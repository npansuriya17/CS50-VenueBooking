
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("profile/<str:p_user>", views.profile, name="profile"),
    path("following", views.following, name="following"),

    # API Routes
    
    #path("allposts/", views.get_posts, name="get_posts"),
    #path("allposts/<str:post_type>", views.get_posts, name="profile"),
    #path("newpost", views.new_post, name="new_post"),
    
]
