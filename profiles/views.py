from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.core.exceptions import MultipleObjectsReturned
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from .models import Name, Posts
# Create your views here.

def add(request):
    if request.method == "GET":
        return render(request, 'profiles/add.html', {'damn': 'daniel'})
    elif request.method == "POST":
        reddit_input = pk=request.POST['reddit']
        name_input = pk=request.POST['name']
        picture_input = pk=request.POST['picture']
        try:
            obj = Name.objects.get(name_text=name_input)
        except MultipleObjectsReturned and Name.DoesNotExist:
            obj = Name(name_text=name_input, reddit=reddit_input, picture=picture_input)
            obj.save()
            return render(request, 'profiles/add.html', {'was_created': 'You\'ve added your profile! Thanks!'})
        return render(request, 'profiles/add.html', {'was_created': 'Already exists!'})

def post(request):
    if request.method == "GET":
        return render(request, 'profiles/post.html')
    elif request.method == "POST":
        title_input = pk=request.POST['title']
        author_input = pk=request.POST['author']
        body_input = pk=request.POST['body']
        img_input = pk=request.POST['img']
        obj = Posts(title_text=title_input, author=author_input, body_text=body_input, img=img_input)
        obj.save()
        return render(request, 'profiles/post.html', {'was_posted': 'Thanks for your post!'})

def postText(request):
    if not request.user.is_authenticated():
        return render(request, 'profiles/login.html')
    else:
        if request.method == "GET":
            return render(request, 'profiles/postText.html')
        elif request.method == "POST":
            title_input = pk=request.POST['title']
            author_input = pk=request.POST['author']
            body_input = pk=request.POST['body']
            logs_input = pk=request.POST['logs']
            obj = Posts(title_text=title_input, author=author_input, body_text=body_input, log_text=logs_input)
            obj.save()
            return render(request, 'profiles/postText.html', {'was_posted': 'Thanks for your post!'})

def posts(request):
    latest_post_list = Posts.objects.all()
    template = loader.get_template('profiles/index.html')
    context = {
        'all_posts': latest_post_list
    }
    return HttpResponse(template.render(context, request))

def thread(request, thread_name):
    get_thread = Posts.objects.filter(title_text=thread_name)
    return render(request, 'profiles/thread.html', {'thread': get_thread})


#User stuff
def register(request):
    return render(request, 'profiles/register.html')

def registerUser(request):
    if request.method == "GET":
        return render(request, 'profiles/index.html')
    elif request.method == "POST":
        uname_input = pk=request.POST['name']
        email_input = pk=request.POST['email']
        password_input = pk=request.POST['password']
        user = User.objects.create_user(uname_input, email_input, password_input)
        user.save()
        return render(request, 'profiles/register.html', {'was_registered': 'Thanks for your registration!'})

def signin(request):
    if not request.user.is_authenticated():
        return render(request, 'profiles/login.html')
    else:
        return render(request, 'profiles/index.html')

def loginUser(request):
    if request.method == "GET":
        return render(request, 'profiles/index.html')
    elif request.method == "POST":
        uname_input = request.POST['username']
        password_input = request.POST['password']
        user = authenticate(username=uname_input, password=password_input)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'profiles/login.html', {'was_logged': 'Thanks for logging in!'})
            else:
                return render(request, 'profiles/login.html', {'was_logged': 'You\'ve been banned.'})
        else:
            return render(request, 'profiles/login.html', {'was_logged': 'That, my friend, is an incorrect login.'})

def logout_view(request):
    logout(request)
    return render(request, 'profiles/index.html')
