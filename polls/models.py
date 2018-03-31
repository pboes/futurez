from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Claim(models.Model):
	"""
	every claim gets its model instance
	"""	
    text = models.TextField(max_length=200, blank=False)
    time_created = models.DateTimeField(auto_now_add=True)
    right_answer = models.NullBooleanField()
    yes = models.IntegerField(default=0)
    no = models.IntegerField(default=0)
    skip = models.IntegerField(default=0)
    reported = models.IntegerField(default=0)
    blocked = models.BooleanField(default=False)
    user = models.ForeignKey(
        User, default=None, null=True, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.text


class Vote(models.Model):
	"""
	This model connects claims to users 
	"""
    user = models.ForeignKey(
        User, default=None, null=True, on_delete=models.CASCADE)
    claim = models.ForeignKey(Claim, on_delete=models.CASCADE)
    vote = models.NullBooleanField()


class Report(models.Model):
	"""
	Collect reported claims and block reported claims
	"""
    user = models.ForeignKey(
        User, default=None, null=True, on_delete=models.CASCADE)
    claim = models.ForeignKey(Claim, on_delete=models.CASCADE)


class Submission(models.Model):
	"""
	Model for submissions to decided claims.
	"""
    claim = models.ForeignKey(Claim, on_delete=models.CASCADE)
    comment = models.TextField(max_length=500, blank=True)
    evidence = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    submitted_answer = models.NullBooleanField()
    status = models.BooleanField(default=True)

# #these two are to make sure that we a) automatically create a profile instance once we create a user instance and b) we can update the profile through the user. see https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
