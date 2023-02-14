from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator
import json
from django.http import JsonResponse

from .models import User, Post, Follow, Likes


def index(request):
    allPosts = Post.objects.all().order_by('-timestamp')

    # create paginator
    paginator = Paginator(allPosts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # create list of post.id-s which current user liked
    allLikedObjects = Likes.objects.all()
    postList = []
    try:
        for likedObject in allLikedObjects:
            if likedObject.likedBy == request.user:
                postList.append(likedObject.post.id)
    except:
        postList = []

    if request.method == "GET":
        if request.user.is_authenticated:
            return render(request, "network/index.html", {
                "page_obj": page_obj,
                "postList": postList

            })
        else: 
            return HttpResponseRedirect(reverse("login"))



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


def post(request):

    # add new post
    if request.method == 'POST':
        currUser = request.user
        data = request.POST["postTextarea"]
        createPost = Post.objects.create(creator = currUser, content = data)
        createPost.save()


        return HttpResponseRedirect(reverse("index"))

def profile(request, username):
    # get user by username which was provided from 'index' function to html and from html to url
    profileUser = User.objects.get(username=username)
    postsByThisUser = Post.objects.filter(creator=profileUser).order_by('-timestamp')

    # lets create list of post.id-s which current user liked
    allLikedObjects = Likes.objects.all()
    postList = []
    try:
        for likedObject in allLikedObjects:
            if likedObject.likedBy == request.user:
                postList.append(likedObject.post.id)
    except:
        postList = []



    # create paginator for posts
    paginator = Paginator(postsByThisUser, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    # we know on what profile we are on, so, lets get every Follow object, who has this profile as a followreciever 
    profileUserFollowers = Follow.objects.filter(followReceiver = profileUser)

    # get the current user in browser
    currentUser = User.objects.get(pk=request.user.id)

    # count followers and following
    followerCount = len(profileUserFollowers)
    profileUserFollowing = Follow.objects.filter(follower = profileUser)
    followingCount = len(profileUserFollowing)

    

    try:
        # now, in those objects, lets filter all of them, which has current user in Follower instance
        checkFollowing = profileUserFollowers.filter(follower = currentUser)
        # if we get list longer than 0, it means current user follows profile user
        if len(checkFollowing) != 0:
            follows = True
        else:
            follows = False
    
    except:
        follows = False



     

    return render(request, "network/profile.html", {
        "profileUser": profileUser,
        "page_obj": page_obj,
        "follows": follows,
        "followerCount": followerCount,
        "followingCount": followingCount,
        "postList": postList
    })


def follow(request, followreceiver):
    follower = request.user
    followReceiver = User.objects.get(username=followreceiver)
    makeContact = Follow.objects.create(follower = follower, followReceiver = followReceiver)
    makeContact.save()

    return HttpResponseRedirect(reverse("profile", kwargs={
        "username": followreceiver
    }))


def unfollow(request, followreceiver):
    follower = request.user
    followReceiver = User.objects.get(username=followreceiver)
    deleteContact = Follow.objects.get(follower = follower, followReceiver = followReceiver)
    deleteContact.delete()

    return HttpResponseRedirect(reverse("profile", kwargs={
        "username": followreceiver
    }))


def followPage(request):
    currUser = request.user

    # get objects where we are followers
    userIsFollower = Follow.objects.filter(follower = currUser)

    # loop over arrays of objects and create new array of users we are following
    userFollows = []
    for object in userIsFollower:
        userFollows.append(object.followReceiver)

    # get all the posts
    allPosts = Post.objects.all().order_by('-timestamp')
    followingPosts = []
    
    for post in allPosts:
        for user in userFollows:
            if user == post.creator:
                followingPosts.append(post)

    # create paginator
    paginator = Paginator(followingPosts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # create list of post.id-s which current user liked
    allLikedObjects = Likes.objects.all()
    postList = []
    try:
        for likedObject in allLikedObjects:
            if likedObject.likedBy == request.user:
                postList.append(likedObject.post.id)
    except:
        postList = []

    
    return render(request, "network/following.html", {
        "page_obj": page_obj,
        "postList": postList
    })

        

def editText(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        textData = data['textareaValue']
        postID = data['postID']
        post = Post.objects.get(pk=postID)
        post.content = textData
        post.save()


    return JsonResponse({"message": "Success", "data": textData})


def like(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        postID = data['postid']
        post = Post.objects.get(pk=postID)
        likedBy = request.user
        createLike = Likes.objects.create(post = post, likedBy = likedBy)
        createLike.save()

        # now, lets get every likes object, which has our post object in post's field
        totalLikes = len(post.likedPost.all())

        # check if current user is in likes of this post
        if post.likedPost.filter(likedBy = likedBy).exists():
            liked = True
        else:
            liked = False


        
        
  
        
    return JsonResponse({"message": "Success", "likes": totalLikes, "liked": liked})

def unlike(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        postID = data['postid']
        post = Post.objects.get(pk = postID)
        likedObject = Likes.objects.filter(post = post, likedBy = request.user)
        likedObject.delete()

        totalLikes = len(post.likedPost.all())


    return JsonResponse({"message": "Success", "likes": totalLikes})

def editProfile(request):
    if request.method == "GET":
        return render(request, "network/editprofile.html")
    
    elif request.method == "POST":
        user = request.user
        newProf = request.FILES['newProfPic']
        user.profilePicture = newProf
        user.save()
        return HttpResponseRedirect(reverse("editProfile"))
