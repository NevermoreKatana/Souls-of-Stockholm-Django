from souls_of_stockholm.user.models import CustomUser
from souls_of_stockholm.user import services
from souls_of_stockholm.user.forms import RegistrationForm
from django.contrib.auth import logout
from souls_of_stockholm.posts.models import Posts
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.shortcuts import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model


class UserView(ListView):
    model = get_user_model()
    template_name = 'user/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = CustomUser.objects.get(id=self.kwargs['id'])
        post = Posts.objects.filter(author=self.kwargs['id'])
        context['posts'] = post
        context['user'] = user
        context['user_id'] = self.request.session.get('user_id')
        context['is_session_active'] = 'user_id' in self.request.session
        return context


class CreateUserView(CreateView):
    model = get_user_model()
    template_name = 'user/register.html'
    form_class = RegistrationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_session_active'] = 'user_id' in self.request.session
        context['user_id'] = self.request.session.get('user_id')
        return context

    def generate_tokens(self, user):
        refresh = RefreshToken.for_user(user)
        token = {
            'access': str(refresh.access_token)
        }
        return token['access']

    def form_valid(self, form):
        password = form.cleaned_data['password']
        password_confirm = form.cleaned_data['confirm_password']
        errors = services.check_errors(password, password_confirm)
        if errors:
            messages.error(self.request, errors)
            return self.form_invalid(form)

        jwt = self.generate_tokens(form.instance)
        form.instance.jwt = jwt
        form.instance.password = make_password(password)
        messages.success(self.request, 'Пользователь успешно зарегистрирован')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('login')


class UpdateUserView(UpdateView):
    model = get_user_model()
    template_name = 'user/update.html'
    form_class = RegistrationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_session_active'] = 'user_id' in self.request.session
        context['user_id'] = self.request.session.get('user_id')
        return context

    def form_valid(self, form):
        password = form.cleaned_data['password']
        password_confirm = form.cleaned_data['confirm_password']
        errors = services.check_errors(password, password_confirm)
        if errors:
            messages.error(self.request, errors)
            return self.form_invalid(form)

        form.instance.password = make_password(password)
        messages.success(self.request, 'Пользователь успешно обновлен')
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        user = self.get_object()
        if user.id != self.request.session.get('user_id'):
            messages.error(self.request, 'Вы не можете редактировать данного юзера')
            return HttpResponseRedirect(reverse('main'))
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        user_id = self.request.session.get('user_id')
        return reverse('profile', kwargs={'id': user_id})


class DeleteUserView(DeleteView):
    model = get_user_model()
    template_name = 'user/delete.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_session_active'] = 'user_id' in self.request.session
        context['user_id'] = self.request.session.get('user_id')
        return context

    def dispatch(self, request, *args, **kwargs):
        user = self.get_object()
        if user.id != self.request.session.get('user_id'):
            messages.error(self.request, 'Вы не можете редактировать данного юзера')
            return HttpResponseRedirect(reverse('main'))
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        messages.success(self.request, 'Пользователь успешно удален')
        logout(self.request)
        return reverse('main')
