from django.urls import path
from souls_of_stockholm.forums import views

urlpatterns = [
    path('', views.ForumsView.as_view(), name='forums_index'),
    path('<int:id>/', views.OneTagPostsView.as_view(), name='forum_tag_filer')
]
