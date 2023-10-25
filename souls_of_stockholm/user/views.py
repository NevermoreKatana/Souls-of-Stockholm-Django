from django.shortcuts import render, redirect
from django.views import View
from souls_of_stockholm.user.models import CustomUser
from souls_of_stockholm.user import services
from souls_of_stockholm.user.forms import RegistrationForm


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
        form = RegistrationForm()
        return render(request, 'user/register.html', {'is_session_active': is_session_active, 'user_id': user_id, 'form': form})

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)
        errors = services.create_user(request, CustomUser, form)
        return errors
