from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
import json

from .models import Claim

def poll(request, no):
	if no == '':
		claim = Claim.objects.filter(right_answer = None).order_by("time_created").reverse()[0]
	else:
		claim = Claim.objects.get(pk=no)
	#ClaimForm = modelformset_factory(Claim, fields=('text', 'yes', 'no'))   
	if request.method == 'POST':

		#claim_id = int(request.POST['claim-id'])
		new_claim = Claim.objects.get(pk= no)
		try:
			next_claim = Claim.objects.filter(pk__gt = no).filter(right_answer = None).order_by("pk")[0]
		except:
			next_claim = Claim.objects.filter(right_answer = None).order_by("pk")[0]
		print next_claim.id
		if request.POST.has_key("skip"):
			return HttpResponseRedirect(reverse("polls:poll", args=(next_claim.id,)))
		elif request.POST.has_key("yes"):
			new_claim.yes += 1
			new_claim.save()

			return HttpResponseRedirect(reverse("polls:poll", args=(next_claim.id,)))

		elif request.POST.has_key("no"):
			new_claim.no += 1
			new_claim.save()

			return HttpResponseRedirect(reverse("polls:poll", args=(next_claim.id,)))

	else:
		return render(request, 'polls/poll.html', {'claim': claim})

def add_claim(request):
    if request.method == 'POST':
        print request.POST
        claim = Claim(text= request.POST['text'])
        claim.save()
        return HttpResponse(
                json.dumps(claim.id),
                content_type="application/json"
            )

    else:
        return HttpResponse(
                json.dumps({"nothing to see": "this isn't happening"}),
                content_type="application/json"

            )

def home(request):
	claims = Claim.objects.all().order_by("time_created").reverse()
	return render(request, 'polls/polls_home.html', {'claims': claims})	










