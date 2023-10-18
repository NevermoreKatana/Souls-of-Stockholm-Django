from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from souls_of_stockholm.posts.models import Posts
from django.contrib import messages

class IndexView(View):

    def get(self, request, *args, **kwargs):
        is_session_active = 'user_id' in request.session
        user_id = request.session.get('user_id')
        posts = Posts.objects.all()
        return render(request, 'index.html', {'is_session_active': is_session_active, 'posts': posts, 'user_id': user_id})


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):
        username = request.POST.get('uname')
        password = request.POST.get('passwd')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            return redirect('main')
        messages.error(request, 'Не правильный логин или пароль')
        return redirect('login')


class LogoutView(View):
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('main')