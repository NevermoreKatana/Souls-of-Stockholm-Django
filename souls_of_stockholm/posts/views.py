from django.shortcuts import render, redirect
from django.views import View
from souls_of_stockholm.user.models import CustomUser
from souls_of_stockholm.posts.models import Posts, Comments
from souls_of_stockholm.services import handle_error, handle_success
from django.contrib import messages
from souls_of_stockholm.posts import services
from souls_of_stockholm.posts.models import Tag
class PostView(View):
    def get(self, request, *args, **kwargs):
        post_id = kwargs.get('id')
        is_session_active = 'user_id' in request.session
        posts = Posts.objects.get(id=post_id)
        user_id = request.session.get('user_id')
        comments = Comments.objects.filter(post__id=post_id)
        return render(request, 'posts/post.html', {'is_session_active': is_session_active, 'posts': posts, 'user_id': user_id, 'comments': comments})

    def post(self, request, *args, **kwargs):
        is_session_active = 'user_id' in request.session
        post_id = kwargs.get('id')
        if not is_session_active:
            return handle_error(request, 'Чтобы писать комментарии пройдите аутентификацию', 'login')
        return services.add_comments(request, post_id)

class PostCreateView(View):

    def get(self, request, *args, **kwargs):
        is_session_active = 'user_id' in request.session
        tags = Tag.objects.all()
        if not is_session_active:
            return handle_error(request, 'Чтобы создать пост пройдите аутентификацию', 'login')
        user_id = request.session.get('user_id')
        return render(request, 'posts/create.html', {'is_session_active': is_session_active, 'user_id': user_id, 'tags': tags})

    def post(self, request, *args, **kwargs):
        return services.create_post(request)


