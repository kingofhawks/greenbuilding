from django.forms import ModelForm
from models import Project


#Create form from models
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'user']
