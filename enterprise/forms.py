from django.forms import ModelForm
from models import Project, Submission, ApplicationReview


#Create form from models
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        #fields = ['name', 'description', 'user']


class SubmissionForm(ModelForm):
    class Meta:
        model = Submission
        exclude = ['date']


class ReviewForm(ModelForm):
    class Meta:
        model = ApplicationReview
        exclude = ['date']