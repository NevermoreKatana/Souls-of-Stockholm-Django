from django.urls import path
from souls_of_stockholm.api import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [
    path('posts/', views.PostsListView.as_view(), name='post_list'),
    path('authorization/', views.PersonalUserListView.as_view(), name='personal_user'),
    path('token/', TokenObtainPairView.as_view(), name='authorization'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('post/<int:id>/', views.OnePostListView.as_view(), name='one_post'),
    path('post/<int:id>/comment/add', views.CommentListCreateView.as_view(), name='add_comment'),
    path('user/<int:id>/', views.ShowUserListView.as_view(), name='user'),
]
