from souls_of_stockholm.user.validator import check_password, check_len_password
from souls_of_stockholm.user.jwt import generate_tokens
from django.db import IntegrityError
from souls_of_stockholm.services import handle_error, handle_success


def check_errors(password1, password2, age, request):
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
    errors = check_errors(password1, password2, age, request)
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









