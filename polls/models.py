from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
#from django.db.models.signals import post_save
#from django.dispatch import receiver

# Create your models here.
class Claim(models.Model):

	text = models.TextField(max_length=200, blank=False)
	time_created = models.DateTimeField(auto_now_add=True)
	right_answer = models.NullBooleanField()
	yes = models.IntegerField(default=0)
	no = models.IntegerField(default=0)
	skip = models.IntegerField(default=0)
	reported = models.IntegerField(default=0)
	blocked = models.BooleanField(default=False)
	user = models.ForeignKey(User, default=None, null=True, on_delete=models.CASCADE)

	def __unicode__(self):
		return self.text

class Vote(models.Model):
	user = models.ForeignKey(User, default=None, null=True, on_delete=models.CASCADE)
	claim = models.ForeignKey(Claim, on_delete=models.CASCADE)
	vote = models.NullBooleanField()

class Report(models.Model):
	user = models.ForeignKey(User, default=None, null=True, on_delete=models.CASCADE)
	claim = models.ForeignKey(Claim, on_delete=models.CASCADE)

class Submission(models.Model):
	claim = models.ForeignKey(Claim, on_delete=models.CASCADE)
	comment = models.TextField(max_length=500, blank=True)
	evidence = models.TextField(max_length=500)
	user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
	submitted_answer = models.NullBooleanField()
	status = models.BooleanField(default=True)

# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')

# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     #yes_claims = models.ManyToManyField(Claim, related_name='yes_claim', default=None)
#     #no_claims = models.ManyToManyField(Claim, related_name='no_claim', default=None)	

# #these two are to make sure that we a) automatically create a profile instance once we create a user instance and b) we can update the profile through the user. see https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()