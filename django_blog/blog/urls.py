from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

from .views import (
    PostListView, PostDetailView, PostCreateView,
    PostUpdateView, PostDeleteView
)

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="accounts/logout.html"), name="logout"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
    path("profile/edit/", views.profile_edit, name="profile_edit"),
    
    #for posts CRUD operation
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-edit'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
