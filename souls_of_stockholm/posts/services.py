from souls_of_stockholm.services import handle_error, handle_success
from souls_of_stockholm.posts.models import Posts, Comments
from souls_of_stockholm.user.models import CustomUser
from django.shortcuts import redirect
from souls_of_stockholm.posts.models import Tag

def add_comments(request, post_id):
    user_id = request.session.get('user_id')
    coment = request.POST.get('comment')
    post = Posts.objects.get(id=post_id)
    user = CustomUser.objects.get(id=user_id)
    comment = Comments()
    comment.user = user
    comment.post = post
    comment.content = coment
    comment.save()
    return redirect(request.get_full_path())


def create_post(request):
    post_name = request.POST.get('name')
    content = request.POST.get('content')
    tags = request.POST.getlist('tags')
    post = Posts()
    post.content = content
    post.name = post_name
    post.user = CustomUser.objects.get(id=request.session.get('user_id'))
    post.save()
    for tags_id in tags:
        tag = Tag.objects.get(id=tags_id)
        post.tag.add(tag)
    return redirect('main')
