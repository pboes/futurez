"""claim_and_wonder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path

from . import views

urlpatterns = [
    path(r'add_claim', views.add_claim, name="add_claim"),
    path(r'vote', views.vote, name="vote"),
    path(r'', views.poll, name="poll"),
    path(r'<int:no>', views.poll, name="poll"),
    # path(r'home', views.home, name="home"),
    path(r'end_of_line', views.end_of_line, name="end_of_line"),
    path(r'profile', views.user_home, name="user_home"),
    path(r'report', views.report, name="report"),
    path(r'submissions', views.submissions, name="submissions"),
    path(r'decide', views.decide, name="decide"),
    	]