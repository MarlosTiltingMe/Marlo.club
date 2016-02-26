from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.core.exceptions import MultipleObjectsReturned
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from .models import Posts
# Create your views here.

def post(request):
    if not request.user.is_authenticated():
        return render(request, 'profiles/login.html')
    else:
        if request.method == "GET":
            return render(request, 'profiles/post.html', {'name': request.user})
        elif request.method == "POST":
            title_input = pk=request.POST['title']
            author_input = request.user
            body_input = pk=request.POST['body']
            img_input = pk=request.POST['img']
            obj = Posts(title_text=title_input, author=author_input, body_text=body_input, img=img_input)
            obj.save()
            return render(request, 'profiles/post.html', {'was_posted': 'Thanks for your post!', 'name': request.user})

def postText(request):
    if not request.user.is_authenticated():
        return render(request, 'profiles/login.html')
    else:
        if request.method == "GET":
            return render(request, 'profiles/postText.html')
        elif request.method == "POST":
            title_input = pk=request.POST['title']
            author_input = request.user
            body_input = pk=request.POST['body']
            logs_input = pk=request.POST['logs']
            obj = Posts(title_text=title_input, author=author_input, body_text=body_input, log_text=logs_input)
            obj.save()
            return render(request, 'profiles/postText.html', {'was_posted': 'Thanks for your post!', 'name': request.user})

def posts(request):
    latest_post_list = Posts.objects.all()
    template = loader.get_template('profiles/index.html')
    context = {
        'all_posts': latest_post_list,
        'name': request.user,
    }
    return HttpResponse(template.render(context, request))

def thread(request, thread_name):
    get_thread = Posts.objects.filter(title_text=thread_name)
    return render(request, 'profiles/thread.html', {'thread': get_thread, 'name': request.user})


#User stuff
def register(request):
    if request.user.is_authenticated():
        return render(request, 'profiles/index.html', {'name': request.user})
    else:
        return render(request, 'profiles/register.html')

def registerUser(request):
    if request.method == "GET":
        return render(request, 'profiles/index.html', {'name': request.user})
    elif request.method == "POST":
        uname_input = pk=request.POST['name']
        email_input = pk=request.POST['email']
        password_input = pk=request.POST['password']
        if not User.objects.filter(username = uname_input).exists():
            if not User.objects.filter(email = email_input).exists():
                user = User.objects.create_user(uname_input, email_input, password_input)
                user.save()
                return render(request, 'profiles/register.html', {'was_registered': 'Thanks for your registration!', 'name': request.user})
            return render(request, 'profiles/register.html', {'was_registered': 'That E-Mail already exists.'})
        return render(request, 'profiles/register.html', {'was_registered': 'That name is taken'})

def signin(request):
    if not request.user.is_authenticated():
        return render(request, 'profiles/login.html', {'name': request.user})
    else:
        return render(request, 'profiles/index.html', {'name': request.user})

def loginUser(request):
    if request.method == "GET":
        return render(request, 'profiles/index.html', {'name': request.user})
    elif request.method == "POST":
        uname_input = request.POST['username']
        password_input = request.POST['password']
        user = authenticate(username=uname_input, password=password_input)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'profiles/login.html', {'was_logged': 'Thanks for logging in!', 'name': request.user})
            else:
                return render(request, 'profiles/login.html', {'was_logged': 'You\'ve been banned.', 'name': request.user})
        else:
            return render(request, 'profiles/login.html', {'was_logged': 'That, my friend, is an incorrect login.', 'name': request.user})

def logout_view(request):
    logout(request)
    return render(request, 'profiles/index.html')

def member_view(request):
    member_list = User.objects.all()
    context = {
        'members': member_list,
        'name': request.user,
    }
    return render(request, 'profiles/members.html', context)
