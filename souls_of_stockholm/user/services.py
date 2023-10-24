from souls_of_stockholm.user.validator import check_password, check_len_password
from souls_of_stockholm.user.jwt import generate_tokens
from django.db import IntegrityError
from souls_of_stockholm.services import handle_error, handle_success

def check_errors(request):
    password1 = request.POST.get('passwd')
    password2 = request.POST.get('confirm_passwd')
    age = request.POST.get('age')
    try:
        age = int(age)
    except ValueError:
        return handle_error(request, 'ВОЗРАСТ ЭТО ЦИФРЫ БИМ БИМ БАМ БАМ NOT USE STR USE INT!!!!', 'register')
    if not check_password(password1, password2):
        return handle_error(request,'Пароли не совпадают', 'register')
    elif not check_len_password(password1):
        return handle_error(request, 'Пароль слишком короткий', 'register')

def create_user(request, model):
    username = request.POST.get('uname')
    password1 = request.POST.get('passwd')
    password2 = request.POST.get('confirm_passwd')
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    country = request.POST.get('country')
    errors = check_errors(request)
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









