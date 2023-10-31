from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import logout
from souls_of_stockholm.posts.models import Posts, Tag
from souls_of_stockholm import services
from souls_of_stockholm.forms import CustomUserForm
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

class ForumsView(View):
    def get(self, request, *args, **kwargs):
        is_session_active = 'user_id' in request.session
        user_id = request.session.get('user_id')
        posts = Posts.objects.all()
        tags = Tag.objects.all()
        return render(request, 'forum/index.html', {'is_session_active': is_session_active,
                                              'posts': posts,
                                              'user_id': user_id,
                                              'tags': tags})

    def post(self, request, *args, **kwargs):
        is_session_active = 'user_id' in request.session
        user_id = request.session.get('user_id')
        posts = services.searching_form(request, Posts)
        tags = Tag.objects.all()
        return render(request, 'forum/index.html',
                      {'is_session_active': is_session_active,
                       'posts': posts,
                       'user_id': user_id,
                       'tags': tags})


class OneTagPostsView(View):

    def get(self, request, *args, **kwargs):
        tag_id = kwargs.get('id')
        is_session_active = 'user_id' in request.session
        user_id = request.session.get('user_id')
        posts = Posts.objects.filter(tag=tag_id)
        tags = Tag.objects.all()
        return render(request, 'forum/index.html', {'is_session_active': is_session_active,
                                              'posts': posts,
                                              'user_id': user_id,
                                              'tags': tags})
