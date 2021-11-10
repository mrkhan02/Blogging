from django.shortcuts import render,HttpResponse,redirect
from .models import Contact,Subscribe,Vote
from blog.models import Post
from django.contrib.messages import constants as messages
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout
from django.core.mail import send_mail
from django.conf import settings
import random
import string
import datetime



def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def home(request):
    allPosts=Post.objects.all().filter(status=1)
    n=len(allPosts)
    if(n>4):
        context={'allPosts':allPosts[:n-5:-1]}
    else:
        context={'allPosts':allPosts[::-1]}
    return render(request,"home/index.html",context)
def blog(request):
    return render(request,"home/blog.html")
def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        content=request.POST['content']
        contact= Contact(name=name,email=email,phone=phone,content=content)
        contact.save()
    return render(request,"home/contact.html")
def about(request):
    return render(request,"home/about.html")

def search(request):
    query=request.GET['query']
    if len(query)>78:
        allPosts=Post.objects.none()
    else:
        allPostsTitle= Post.objects.filter(title__icontains=query)
        allPostsAuthor= Post.objects.filter(author__icontains=query)
        allPostsContent =Post.objects.filter(content__icontains=query)
        allPosts=  allPostsTitle.union(allPostsContent, allPostsAuthor)
    if allPosts.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    params={'allPosts': allPosts, 'query': query}
    return render(request, 'home/search.html', params)

def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=get_random_string(8)

        # check for errorneous input
        if len(username)<5:
            messages.error(request, "username lenght is less than 5")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('home')
        # Create the user
        try:
            user= User.objects.get(username=username)

            messages.error(request, "Username already exists")
            return redirect('home')
        except User.DoesNotExist:
            try:
                user= User.objects.get(email=email)

                messages.error(request, "email already exists")
                return redirect('home')
            except User.DoesNotExist:
                myuser = User.objects.create_user(username, email, pass1)
                send_mail(
                '211-Premium Password',
                'Hi '+ fname + ','+ '\n Username: '+username  +'\n  password: '+ pass1,
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
                )

        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        return redirect('/')

    else:
        return HttpResponse("404 - Not found")

def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")

    return HttpResponse("404- Not found")


def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')
def subscribe(request):
    name=request.user.first_name
    email=request.user.email
    try:
        user= Subscribe.objects.get(email=email)
        messages.success(request, "Already subscribed")
        return redirect('home')
    except Subscribe.DoesNotExist:
        subscribe= Subscribe(name=name,email=email)

    subscribe.save()
    send_mail(
    'Welcome to 211-Premium',
    'Hi '+ request.user.first_name+ ','+ '\nThanks for subscribing',
    settings.EMAIL_HOST_USER,
    [request.user.email],
fail_silently=False,
)
    return redirect('home')



def add(request):
    if request.user.is_authenticated:
        return render (request, "home/add.html")
    else:
        return HttpResponse('Page not found')
def added(request):
    if request.method=="POST":
        title=request.POST['title']
        content=request.POST['mytextarea']
        author=request.POST['name']
        img=request.FILES['myfile']
        slug=title+get_random_string(20)
        date=datetime.datetime.now()
        post= Post(title=title,content=content,author=author,slug=slug,image=img,date=date)
        post.save()
        return redirect('home')
