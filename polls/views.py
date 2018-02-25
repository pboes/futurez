from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
import json
from random import randint, choice

from .forms import SubmissionForm
from .models import Claim, Vote, Submission, Report
from django.conf import settings


def landing(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect(reverse("polls:poll"))
	return render(request, 'polls/landing.html')

# @login_required()
def poll(request, no=None):
	if request.user.is_authenticated:
		possible_claims = Claim.objects.filter(blocked=False).filter(right_answer = None).exclude(vote__user = request.user).exclude(report__user=request.user).order_by("pk")
		sam = 0
		if no == None:
			if len(possible_claims) != 0:
				claim = possible_claims.first()
				return HttpResponseRedirect(reverse("polls:poll", args=(possible_claims.first().id,)))
			else:
				return HttpResponseRedirect(reverse("polls:end_of_line"))

	else: 
		possible_claims = Claim.objects.filter(blocked=False).filter(right_answer = None).order_by("pk")
		sam = randint(0,len(possible_claims)-1)
		if no == None:	
			claim = possible_claims[sam]
			return HttpResponseRedirect(reverse("polls:poll", args=(claim.id,)))

	if request.method == 'POST':
		claim = Claim.objects.get(pk= no)
		if "submission" in request.POST:
			submission_form = SubmissionForm(request.POST)
			if submission_form.is_valid():
				submission = submission_form.save(commit = False)
				submission.user = request.user
				submission.claim = claim
				submission.save()
				
		else: 
			claim = Claim.objects.get(pk= no)
			vote = Vote(user=request.user, claim=claim)
			if "skip" in request.POST:
				claim.skip += 1

			elif "yes" in request.POST:
				claim.yes += 1
				vote.vote = True

			elif "no" in request.POST:
				claim.no += 1
				vote.vote = False
			
			claim.save()
			vote.save()
		
		possible_claims = possible_claims.exclude(pk = no)
		if len(possible_claims) != 0:
			next_url = reverse("polls:poll", args=(possible_claims[sam].id,))
		else:
			next_url = reverse("polls:end_of_line")

		return HttpResponseRedirect(next_url)

	claim = Claim.objects.get(pk=no)
	submission_form = SubmissionForm()
	return render(request, 'polls/poll.html', {'claim': claim, 'form':submission_form})


def add_claim(request):
	if request.method == 'POST':
		try:
			if request.user.is_authenticated:
				claim = Claim(text= request.POST['text'], user=request.user)
			else:
				claim = Claim(text= request.POST['text'], user=None)
				claim.save()
				return HttpResponse(
						json.dumps(claim.id),
						content_type="application/json"
					)

		except:
			return HttpResponse(
				json.dumps({"mistake":"mistake"}),
				content_type="application/json"
			)

	else:
		return HttpResponse(
				json.dumps({"nothing to see": "this isn't happening"}),
				content_type="application/json"

			)


def report(request):
	if request.method == 'POST':
		claim = Claim.objects.get(pk=request.POST['no'])
		claim.reported += 1
		report = Report(claim=claim, user= request.user)

		if claim.reported >= settings.REPORT_LIMIT:
			claim.blocked = True

		claim.save()
		report.save()
		return HttpResponse(
				json.dumps({"url": "success"}),
				content_type="application/json"
			)	

	else:
		return HttpResponse(
				json.dumps({"nothing to see": "this isn't happening"}),
				content_type="application/json"
			)	

# @login_required()
def end_of_line(request):
	return render(request, 'polls/end_of_line.html')


@login_required()
def user_home(request):
	claims = Claim.objects.filter(user = request.user).order_by("time_created").reverse()
	votes = Vote.objects.filter(user = request.user).exclude(vote=None).order_by("pk").reverse()
	return render(request, 'polls/profile.html', {'claims': claims, 'votes': votes})	

@staff_member_required
def submissions(request):
	submissions = Submission.objects.filter(status=True)
	return render(request, 'polls/submissions_interface.html', {'submissions': submissions})	

def decide(request):
	if request.method == 'POST':
		print(request)
		submission = Submission.objects.get(pk=request.POST['id'])
		if request.POST['accept']:
			submission.claim.right_answer = submission.submitted_answer
			submission.claim.save()
		
		submission.status = False
		submission.save()

		return HttpResponse(
				json.dumps({"success": "success"}),
				content_type="application/json"
			)	

	else:
		return HttpResponse(
				json.dumps({"nothing to see": "this isn't happening"}),
				content_type="application/json"
			)	

