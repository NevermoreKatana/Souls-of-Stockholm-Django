from django.shortcuts import render, redirect
from django.views import View
from souls_of_stockholm.user.models import CustomUser
from souls_of_stockholm.user import services
from souls_of_stockholm.user.forms import RegistrationForm
from souls_of_stockholm.services import handle_error, handle_success
from django.contrib.auth import logout
from souls_of_stockholm.posts.models import Posts

class UserView(View):
    def get(self, request, *args, **kwargs):
        is_session_active = 'user_id' in request.session
        session_id = request.session.get('user_id')
        user_id = kwargs.get('id')
        post = Posts.objects.filter(author=user_id)
        user = CustomUser.objects.get(id=user_id)
        return render(request, 'user/profile.html', {'is_session_active': is_session_active, 'user': user, 'user_id': session_id, 'posts':post })


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


class UpdateUserView(View):

    def get(self, request, *args, **kwargs):
        is_session_active = 'user_id' in request.session
        user_session_id = request.session.get('user_id')
        user_id = kwargs.get('id')
        if services.check_user_perm(user_session_id, user_id):
            initial_data = services.get_update_user_info(user_id)
            form = RegistrationForm(initial_data)
            return render(request, 'user/update.html', {'is_session_active': is_session_active, 'user_id': user_session_id, 'form': form})
        return handle_error(request, 'У вас нет прав редактировать другого пользователя', 'main')
    def post(self, request, *args, **kwargs):
        user_id = request.session.get('user_id')
        form = RegistrationForm(request.POST)
        errors = services.update_user_info(form, request, user_id)
        return errors



class DeleteUserView(View):

    def get(self, request, *args, **kwargs):
        is_session_active = 'user_id' in request.session
        user_session_id = request.session.get('user_id')
        user_id = kwargs.get('id')
        user = CustomUser.objects.get(id=user_id)
        if services.check_user_perm(user_session_id, user_id):
            return render(request, 'user/delete.html',
                          {'is_session_active': is_session_active, 'user_id': user_session_id, 'user': user})
        return handle_error(request, 'У вас нет прав редактировать другого пользователя', 'main')

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = CustomUser.objects.get(id=user_id)
        user.delete()
        logout(request)
        return handle_success(request, 'Пользователь успешно удален', 'main')