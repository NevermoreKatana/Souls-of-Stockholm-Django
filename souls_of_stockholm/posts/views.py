from django.shortcuts import render
from souls_of_stockholm.posts.models import Posts, Comments
from souls_of_stockholm.services import handle_error
from django.contrib import messages
from souls_of_stockholm.posts import services
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.shortcuts import reverse
from souls_of_stockholm.posts.forms import PostForm
from django.http import HttpResponseRedirect
from souls_of_stockholm.mixins import GetSuccessUrlMixin


class PostView(ListView):
    def get(self, request, *args, **kwargs):
        post_id = kwargs.get('id')
        is_session_active = 'user_id' in request.session
        posts = Posts.objects.get(id=post_id)
        user_id = request.session.get('user_id')
        comments = Comments.objects.filter(post__id=post_id)
        return render(request, 'posts/post.html', {'is_session_active': is_session_active,
                                                   'posts': posts,
                                                   'user_id': user_id,
                                                   'comments': comments})

    def post(self, request, *args, **kwargs):
        is_session_active = 'user_id' in request.session
        post_id = kwargs.get('id')
        if not is_session_active:
            return handle_error(request, 'Чтобы писать комментарии пройдите аутентификацию',
                                'login')
        return services.add_comments(request, post_id)


class PostCreateView(LoginRequiredMixin, GetSuccessUrlMixin, CreateView):
    model = Posts
    template_name = 'posts/create.html'
    form_class = PostForm
    login_url = 'login'
    success_message = ''
    success_url = 'forums_index'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_session_active'] = 'user_id' in self.request.session
        context['user_id'] = self.request.session.get('user_id')
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Пост успешно создан')
        return super().form_valid(form)

    def handle_no_permission(self):
        messages.error(self.request, 'Чтобы создать пост пройдите аутентификацию')
        return super().handle_no_permission()


class DeletePostView(DeleteView, GetSuccessUrlMixin):
    model = Posts
    template_name = 'posts/delete.html'
    context_object_name = 'post'
    success_message = 'Пост успешно удален'
    success_url = 'forums_index'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_session_active'] = 'user_id' in self.request.session
        context['user_id'] = self.request.session.get('user_id')
        return context

    def dispatch(self, request, *args, **kwargs):
        post = self.get_object()
        if post.author != self.request.user:
            messages.error(self.request, 'Вы не можете удалить данный пост')
            return HttpResponseRedirect(reverse('forums_index'))
        return super().dispatch(request, *args, **kwargs)


class UpdatePostView(UpdateView, GetSuccessUrlMixin):
    model = Posts
    template_name = 'posts/update.html'
    form_class = PostForm
    success_message = 'Пост успешно обновлен'
    success_url = 'forums_index'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_session_active'] = 'user_id' in self.request.session
        context['user_id'] = self.request.session.get('user_id')
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        post = Posts.objects.get(id=self.kwargs['pk'])
        tag_ids = list(post.tag.values_list('id', flat=True))
        initial_data = {
            'name': post.name,
            'content': post.content,
            'tag': tag_ids,
        }

        kwargs['initial'] = initial_data
        return kwargs

    def dispatch(self, request, *args, **kwargs):
        post = self.get_object()
        if post.author != self.request.user:
            messages.error(self.request, 'Вы не можете редактировать данный пост')
            return HttpResponseRedirect(reverse('forums_index'))
        return super().dispatch(request, *args, **kwargs)
