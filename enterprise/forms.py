from django.forms import ModelForm
from models import (Project, Submission, ApplicationReview, ElementEvaluationForm, BatchEvaluationForm, StageEvaluationForm,
                    UnitEvaluationForm)


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


class ElementEvaluationFormForm(ModelForm):
    class Meta:
        model = ElementEvaluationForm
        exclude = ['date']


class BatchEvaluationFormForm(ModelForm):
    class Meta:
        model = BatchEvaluationForm
        exclude = ['date']


class StageEvaluationFormForm(ModelForm):
    class Meta:
        model = StageEvaluationForm
        exclude = ['date']


class UnitEvaluationFormForm(ModelForm):
    class Meta:
        model = UnitEvaluationForm
        exclude = ['date']