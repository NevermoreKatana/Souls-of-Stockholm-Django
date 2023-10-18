from django.shortcuts import render, redirect
from django.views import View
from souls_of_stockholm.user.models import CustomUser
from souls_of_stockholm.posts.models import Posts, Comments
from django.contrib import messages

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
        if not is_session_active:
            messages.error(request, 'Чтобы писать комментарии пройдите аутентификацию')
            return redirect('login')
        user_id = request.session.get('user_id')
        post_id = kwargs.get('id')
        coment = request.POST.get('comment')
        post = Posts.objects.get(id=post_id)
        user = CustomUser.objects.get(id=user_id)
        comment = Comments()
        comment.user = user
        comment.post = post
        comment.content = coment
        comment.save()
        return redirect(request.get_full_path())

class PostCreateView(View):

    def get(self, request, *args, **kwargs):
        is_session_active = 'user_id' in request.session
        if not is_session_active:
            messages.error(request, 'Чтобы создать пост пройдите аутентификацию')
            return redirect('login')
        user_id = request.session.get('user_id')
        return render(request, 'posts/create.html', {'is_session_active': is_session_active, 'user_id': user_id})

    def post(self, request, *args, **kwargs):
        postname = request.POST.get('name')
        content = request.POST.get('content')
        post = Posts()
        post.content = content
        post.name = postname
        post.user = CustomUser.objects.get(id=request.session.get('user_id'))
        post.save()
        return redirect('main')


