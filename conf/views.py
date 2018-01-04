from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import LoginForm, SignUpForm
from django.shortcuts import render, redirect
import json

# Create your views here.

# def log_and_create(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = request.POST['text']
#             if request.POST['type'] == 'new':
#                 user = User.objects.create_user(username)
#             elif request.POST['type'] == 'login':
#                 user = authenticate(username)
#                 if user is not None:
#                     login(request, user)
#                 #password = 'password'
#             return HttpResponse(
#                             json.dumps(user.id),
#                             content_type="application/json"
#                         )
#         return HttpResponse(
#                             json.dumps('invalid'),
#                             content_type="application/json"
#                         )
#     else:
#         return HttpResponse(
#                 json.dumps({"nothing to see": "this isn't happening"}),
#                 content_type="application/json"

#             )

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect(reverse("polls:user_home"))
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})