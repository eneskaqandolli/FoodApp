from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm
from .models import Profile

from django.views.generic import ListView

# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Welcome {username}, your are now logged in!")
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "user/register.html", {"form": form})

@login_required
def profilepage(request):
    profile = Profile()
    return render(request, "user/profile.html", {"profile": profile})


