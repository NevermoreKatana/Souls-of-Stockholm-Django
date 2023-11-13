from django.contrib import admin
from souls_of_stockholm.user.models import CustomUser
from souls_of_stockholm.posts.models import Tag, Comments, Posts


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username',)
    search_fields = ['name', 'body']
    list_filter = ["is_staff", "username", "last_login", "date_joined"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']
    list_filter = ["name"]


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('content',)
    search_fields = ['content', 'post']
    list_filter = ["post", "create_at", "user"]


@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['author', 'name', 'content']
    list_filter = ["author", "tag"]
