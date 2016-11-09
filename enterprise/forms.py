from django.forms import ModelForm
from models import (Project, Submission, ApplicationReview, ElementEvaluationForm, BatchEvaluationForm, StageEvaluationForm,
                    UnitEvaluationForm)


# Create form from models
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        #fields = ['name', 'description', 'location', 'area', 'cost', 'structure_type', 'start_date', 'end_date',
        #          'construct_company', 'postal_address', 'zipcode']
        #exclude = ['user']
        fields = '__all__'


class SubmissionForm(ModelForm):
    class Meta:
        model = Submission
        exclude = ['date']
        fields = '__all__'


class ReviewForm(ModelForm):
    class Meta:
        model = ApplicationReview
        exclude = ['date']
        fields = '__all__'


class ElementEvaluationFormForm(ModelForm):
    class Meta:
        model = ElementEvaluationForm
        exclude = ['date']
        fields = '__all__'


class BatchEvaluationFormForm(ModelForm):
    class Meta:
        model = BatchEvaluationForm
        exclude = ['date']
        fields = '__all__'


class StageEvaluationFormForm(ModelForm):
    class Meta:
        model = StageEvaluationForm
        exclude = ['date']


class UnitEvaluationFormForm(ModelForm):
    class Meta:
        model = UnitEvaluationForm
        exclude = ['date']