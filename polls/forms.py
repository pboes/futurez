from polls.models import Claim
from polls.models import Submission
from django.forms import ModelForm, RadioSelect, Textarea


class ClaimForm(ModelForm):
    class Meta:
        model = Claim
        fields = ['text', 'yes', 'no']


SUBMISSION_CHOICES = (
    (0, 'Correct'),
    (1, 'False'),
)


class SubmissionForm(ModelForm):
    class Meta:
        model = Submission
        fields = ['submitted_answer', 'evidence', 'comment']
        widgets = {'submitted_answer': RadioSelect(choices=SUBMISSION_CHOICES), 'evidence': Textarea(
            attrs={'cols': 40, 'rows': 3}), 'comment': Textarea(attrs={'cols': 40, 'rows': 3})}
        labels = {
                  'evidence': "Link some external evidence here.", 'comment': "Further comments."}
