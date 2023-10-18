from django.shortcuts import render, redirect
from django.views import View
from souls_of_stockholm.user.validator import check_password, check_len_password
from souls_of_stockholm.user.models import CustomUser
from django.db import IntegrityError
from django.contrib import messages
from souls_of_stockholm.user.jwt import generate_tokens


class UserView(View):
    def get(self, request, *args, **kwargs):
        is_session_active = 'user_id' in request.session
        session_id = request.session.get('user_id')
        user_id = kwargs.get('id')
        user = CustomUser.objects.get(id=user_id)
        return render(request, 'user/profile.html', {'is_session_active': is_session_active, 'user': user, 'user_id': session_id})


class CreateUserView(View):

    def get(self, request, *args, **kwargs):
        is_session_active = 'user_id' in request.session
        user_id = request.session.get('user_id')
        return render(request, 'user/register.html', {'is_session_active': is_session_active, 'user_id': user_id})

    def post(self, request, *args, **kwargs):
        username = request.POST.get('uname')
        password1 = request.POST.get('passwd')
        password2 = request.POST.get('confirm_passwd')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        country = request.POST.get('country')
        try:
            age = int(age)
        except ValueError:
            messages.error(request, 'ВОЗРАСТ ЭТО ЦИФРЫ БИМ БИМ БАМ БАМ NOT USE STR USE INT!!!!')
            return redirect('register')
        if not check_password(password1, password2):
            messages.error(request, 'Пароли не совпадают')
            return redirect('register')
        elif not check_len_password(password1):
            messages.error(request, 'Пароль слишком короткий')
            return redirect('register')
        try:
            user = CustomUser.objects.create_user(username=username, password=password1,age=age, gender=gender, country=country)
            jwt = generate_tokens(user)
            user.jwt = jwt['access']
            user.save()
            messages.success(request, 'Пользователь успешно зарегестрирован')
            return redirect('login')
        except IntegrityError:
            messages.error(request, 'Пользователь с таким именем уже существует')
            return redirect('register')