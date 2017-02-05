from polls.models import Claim
from django.forms import ModelForm

class ClaimForm(ModelForm):
    class Meta:
        model = Claim
        fields = ['text', 'yes', 'no']