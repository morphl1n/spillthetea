
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("post", views.post, name="post"),
    path("profile/<str:username>", views.profile, name="profile"),
    path("follow/<str:followreceiver>", views.follow, name="follow"),
    path("unfollow/<str:followreceiver>", views.unfollow, name="unfollow"),
    path("following", views.followPage, name="followPage"),
    path("edittext", views.editText, name="editText"),
    path("like", views.like, name="like"),
    path("unlike", views.unlike, name="like"),
    path("editprofile", views.editProfile, name="editProfile")
]
