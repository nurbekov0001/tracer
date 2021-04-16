from django.shortcuts import render, redirect
from .forms import MyUserCreationForm
from django.http import request
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.urls import reverse

from django.views.generic import DetailView

from django.contrib.auth import get_user_model

from django.contrib.auth.mixins import LoginRequiredMixin

from django.core.paginator import Paginator


def login_view(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('project:project_list')
        else:
            context['has_error'] = True
    return render(request, 'login.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('project:project_list')


def register_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = MyUserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('project:project_list')
    else:
        form = MyUserCreationForm()
    return render(request, 'user_create.html', context={'form': form})