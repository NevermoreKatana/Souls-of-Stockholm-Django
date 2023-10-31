from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import logout
from souls_of_stockholm.posts.models import Posts, Tag
from souls_of_stockholm import services
from souls_of_stockholm.forms import CustomUserForm


class IndexView(View):

    def get(self, request, *args, **kwargs):
        is_session_active = 'user_id' in request.session
        user_id = request.session.get('user_id')
        return render(request, 'index.html', {'is_session_active': is_session_active,
                                              'user_id': user_id})

    def post(self, request, *args, **kwargs):
        is_session_active = 'user_id' in request.session
        user_id = request.session.get('user_id')
        posts = services.searching_form(request, Posts)
        return render(request, 'index.html',
                      {'is_session_active': is_session_active,
                       'posts': posts,
                       'user_id': user_id})


class LoginView(View):
    def get(self, request, *args, **kwargs):
        form = CustomUserForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = CustomUserForm(request.POST)
        if services.login_user(request, form):
            return services.handle_success(request,
                                           'Вы успешно залогинены',
                                           'main')
        return services.handle_error(request,
                                     'Не правильный логин или пароль',
                                     'login')


class LogoutView(View):
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('main')


