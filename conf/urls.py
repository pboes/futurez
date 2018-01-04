from django.urls import path, include

from . import views

urlpatterns = [
	path(r'signup/', views.signup, name='signup'),

]
