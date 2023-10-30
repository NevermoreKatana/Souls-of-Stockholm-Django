from django.contrib import messages
from django.shortcuts import redirect
from django.db.models import Q
from django.contrib.auth import authenticate, login


def handle_error(request, message, redirect_url):
    messages.error(request, message)
    return redirect(redirect_url)


def handle_success(request, message, redirect_url):
    messages.success(request, message)
    return redirect(redirect_url)


def searching_form(request, model):
    query = request.POST.get('query')
    posts = model.objects.filter(
        Q(name__startswith=query)
        | Q(content__startswith=query)
        | Q(content__endswith=query)
        | Q(name__endswith=query))

    return posts


def login_user(request, form):
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            return True
    return False
