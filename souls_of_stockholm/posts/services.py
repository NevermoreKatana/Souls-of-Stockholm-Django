from souls_of_stockholm.posts.models import Posts, Comments
from souls_of_stockholm.user.models import CustomUser
from django.shortcuts import redirect
from souls_of_stockholm.posts.models import Comments
import re

regular_pattern = r'@gpt'


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


def gpt_answer(form):
    post_content = form.cleaned_data['content']
    result_expression = re.search(regular_pattern, post_content, re.I|re.X)
    if not result_expression:
        return False
    return True


def add_gpt_answer_comment(answer, form):
    result = gpt_answer(form)
    if not result:
        return
    gpt = CustomUser.objects.get(username='GPT')
    comment = Comments(post=form.instance, user=gpt, content=answer)
    comment.save()

