import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from network.models import User, Posts, Likes, Follow
from django.core.serializers import serialize, get_serializer
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from .models import User


def index(request):
    posts = Posts.objects.all().order_by("-posted_time")
    likes = []
    total_likes = []
    post_to_edit = []
    updated_post_id = 0
    liked_post_id = 0
    if request.method == "POST":
        #print(request.POST)
        #print(request.POST["post-id"])
        if "btn-new-post" in request.POST:
            newpost = Posts(
                posted_by_user=request.user,
                content=request.POST["new-post-content"]
            )
            newpost.save()
        elif "btn-like" in request.POST:
            post_to_like = Posts.objects.get(id=request.POST["post-id"])
            newlike = Likes(post=post_to_like,liked_by_user=request.user)
            newlike.save()
            liked_post_id = request.POST["post-id"]
        elif "btn-unlike" in request.POST:
            post_to_unlike = Posts.objects.get(id=request.POST["post-id"])
            Likes.objects.filter(post=post_to_unlike).filter(liked_by_user=request.user).delete()
            liked_post_id = request.POST["post-id"]
        elif "btn-edit-post" in request.POST:
            post_to_edit = Posts.objects.get(id=request.POST["edit-post-id"])
        elif "btn-save-edited-post" in request.POST:
            edited_post = Posts.objects.get(id=request.POST["save-edited-post-id"])
            edited_post.content = request.POST["edit-post-content"]
            edited_post.save(update_fields=['content'])
            updated_post_id = request.POST["save-edited-post-id"]
    for eachpost in posts:
        like = Likes.objects.filter(post__id=eachpost.id).filter(liked_by_user__username=str(request.user))
        like_count = Likes.objects.filter(post__id=eachpost.id).count()
        if like:
            isLiked = True
        else:
            isLiked = False
        likes.append(isLiked)
        total_likes.append(like_count)
    content = zip(posts, likes, total_likes)
    return render(request, "network/index.html", {
        "content" : content,
        "post_to_edit" : post_to_edit,
        "updated_post_id" : updated_post_id,
        "liked_post_id" : liked_post_id
    })


def profile (request, p_user):
    current_user = str(request.user)
    following = Follow.objects.filter(follower__username=current_user).filter(following__username=p_user)
    if following:
        isFollowed = True
    else:
        isFollowed = False
    posts = Posts.objects.filter(posted_by_user__username=p_user).order_by("-posted_time")
    likes = []
    total_likes = []
    post_to_edit = []
    updated_post_id = 0
    liked_post_id = 0
    if request.method == "POST":
        if "btn-unfollow" in request.POST:
            Follow.objects.filter(follower__username=current_user).filter(following__username=p_user).delete()
        elif "btn-follow" in request.POST:
            follow = Follow(following=User.objects.get(username=p_user),follower=User.objects.get(username=current_user))
            follow.save()
        elif "btn-like" in request.POST:
            post_to_like = Posts.objects.get(id=request.POST["post-id"])
            newlike = Likes(post=post_to_like,liked_by_user=request.user)
            newlike.save()
            liked_post_id = request.POST["post-id"]
        elif "btn-unlike" in request.POST:
            post_to_unlike = Posts.objects.get(id=request.POST["post-id"])
            Likes.objects.filter(post=post_to_unlike).filter(liked_by_user=request.user).delete()
            liked_post_id = request.POST["post-id"]
        elif "btn-edit-post" in request.POST:
            post_to_edit = Posts.objects.get(id=request.POST["edit-post-id"])
        elif "btn-save-edited-post" in request.POST:
            edited_post = Posts.objects.get(id=request.POST["save-edited-post-id"])
            edited_post.content = request.POST["edit-post-content"]
            edited_post.save(update_fields=['content'])
            updated_post_id = request.POST["save-edited-post-id"]
    for eachpost in posts:
        like = Likes.objects.filter(post__id=eachpost.id).filter(liked_by_user__username=str(request.user))
        like_count = Likes.objects.filter(post__id=eachpost.id).count()
        if like:
            isLiked = True
        else:
            isLiked = False
        likes.append(isLiked)
        total_likes.append(like_count)
    content = zip(posts, likes, total_likes)
    return render(request, "network/profile.html", {
        "content" : content,
        "isFollowed": isFollowed,
        "p_user": p_user.capitalize(),
        "isMyProfile": p_user == current_user,
        "followers": Follow.objects.filter(following__username=p_user).count(),
        "following": Follow.objects.filter(follower__username=p_user).count(),
        "post_to_edit" : post_to_edit,
        "updated_post_id" : updated_post_id,
        "liked_post_id" : liked_post_id
    })

#{% url 'profile' post.posted_by_user.username %}

def following(request):
    current_user = str(request.user)
    following_users = Follow.objects.filter(follower__username=current_user).values("following")
    allposts = []
    likes = []
    total_likes = []
    liked_post_id = 0
    if request.method == "POST":
        if "btn-like" in request.POST:
            post_to_like = Posts.objects.get(id=request.POST["post-id"])
            newlike = Likes(post=post_to_like,liked_by_user=request.user)
            newlike.save()
            liked_post_id = request.POST["post-id"]
        elif "btn-unlike" in request.POST:
            post_to_unlike = Posts.objects.get(id=request.POST["post-id"])
            Likes.objects.filter(post=post_to_unlike).filter(liked_by_user=request.user).delete()
            liked_post_id = request.POST["post-id"]
    for users in following_users:
        posts = Posts.objects.filter(posted_by_user__id=users["following"])
        for eachpost in posts:
            allposts.append(eachpost)
            print(eachpost)        
    for eachpost in allposts:
        like = Likes.objects.filter(post__id=eachpost.id).filter(liked_by_user__username=str(request.user))
        like_count = Likes.objects.filter(post__id=eachpost.id).count()
        if like:
            isLiked = True
        else:
            isLiked = False
        likes.append(isLiked)
        total_likes.append(like_count)
    print(allposts)
    content = zip(allposts, likes, total_likes)
    return render(request, "network/following.html", {
        "content" : content,
        "liked_post_id" : liked_post_id
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")
