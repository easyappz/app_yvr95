from django.urls import path
from .views import (
    RegisterView,
    LoginView,
    LogoutView,
    ProfileView,
    PostListCreateView,
    PostRetrieveUpdateDestroyView,
    LikeView,
    CommentListCreateView,
    CommentRetrieveUpdateDestroyView
)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("posts/", PostListCreateView.as_view(), name="post-list-create"),
    path("posts/<int:pk>/,", PostRetrieveUpdateDestroyView.as_view(), name="post-retrieve-update-destroy"),
    path("likes/", LikeView.as_view(), name="like"),
    path("comments/", CommentListCreateView.as_view(), name="comment-list-create"),
    path("comments/<int:pk>/", CommentRetrieveUpdateDestroyView.as_view(), name="comment-retrieve-update-destroy"),
]
