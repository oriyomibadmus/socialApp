from django.shortcuts import render, redirect
from .models import Post

def index(request):
    posts = Post.objects.all()
    return render(request, "subApp/index.html", {'posts': posts })

def post(request):
    return render(request, "subApp/post.html")

def profile(request):
    return render(request, "subApp/profile.html")
