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
