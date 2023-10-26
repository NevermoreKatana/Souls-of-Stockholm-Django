from souls_of_stockholm.user.validator import check_password, check_len_password
from souls_of_stockholm.user.jwt import generate_tokens
from django.db import IntegrityError
from souls_of_stockholm.services import handle_error, handle_success
from souls_of_stockholm.user.models import CustomUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth import logout



def check_errors(password1, password2, request):
    if not check_password(password1, password2):
        return handle_error(request,'Пароли не совпадают', 'register')
    elif not check_len_password(password1):
        return handle_error(request, 'Пароль слишком короткий', 'register')


def create_user(request, model, form):
    if not form.is_valid():
        return
    username = form.cleaned_data['username']
    password1 = form.cleaned_data['password']
    password2 = form.cleaned_data['confirm_password']
    age = form.cleaned_data['age']
    gender = form.cleaned_data['gender']
    country = form.cleaned_data['country']
    errors = check_errors(password1, password2, request)
    if errors:
        return errors
    try:
        user = model.objects.create_user(username=username, password=password1,age=age, gender=gender, country=country)
        jwt = generate_tokens(user)
        user.jwt = jwt['access']
        user.save()
        return handle_success(request, 'Пользователь успешно зарегестрирован', 'login')
    except IntegrityError:
        return handle_error(request, 'Пользователь с таким именем уже существует', 'register')


def get_update_user_info(user_id):
    user = CustomUser.objects.values('username', 'age', 'gender', 'country').filter(id=user_id)
    user = list(user)
    return initial_user_data(user[0])


def initial_user_data(user_data):
    initial_data = {
        'username': user_data['username'],
        'age': user_data['age'],
        'gender': user_data['gender'],
        'country': user_data['country'],
    }
    return initial_data


def update_user_info(form, request, user_id):
    if not form.is_valid():
        return
    username = form.cleaned_data['username']
    password1 = form.cleaned_data['password']
    password2 = form.cleaned_data['confirm_password']
    age = form.cleaned_data['age']
    gender = form.cleaned_data['gender']
    country = form.cleaned_data['country']
    errors = check_errors(password1, password2, request)
    if errors:
        return errors
    user = CustomUser.objects.get(id=user_id)
    user.username = username
    user.password = make_password(password1)
    user.age = age
    user.country = country
    user.gender = gender
    logout(request)
    try:
        user.save()
        return handle_success(request, 'Пользователь успешно обновлен', 'login')
    except IntegrityError:
        return handle_error(request, 'Данное имя занято другим пользователем', 'update_user')


def check_user_perm(user_session_id, user_id):
    if user_session_id is user_id:
        return True
    return False
