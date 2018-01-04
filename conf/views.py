from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from .forms import SignUpForm
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

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