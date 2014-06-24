from django.shortcuts import render, redirect
from models import Submission,Project,ApplicationReview,SelfEvaluation,Selection
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from forms import ProjectForm
from django.utils.translation import ugettext as _


class ProjectList(ListView):
    model = Project
    template_name = 'project_list.html'
    context_object_name = 'projects'


class SubmissionList(ListView):
    model = Submission
    template_name = 'submission_list.html'
    context_object_name = 'projects'


class ApplicationReviewList(ListView):
    model = ApplicationReview
    template_name = 'review_list.html'
    context_object_name = 'projects'


class SelfEvaluationList(ListView):
    model = SelfEvaluation
    template_name = 'self_evaluation_list.html'
    context_object_name = 'projects'


class SelectionList(ListView):
    model = Selection
    template_name = 'selection_list.html'
    context_object_name = 'projects'


# Create your views here.
def  new_list(request, template="submission_list.html"):
    submission_list = Submission.objects.all()
    print submission_list
    paginator = Paginator(submission_list, 25) # Show 25 contacts per page
    page = request.GET.get('page')
    print page
    try:
        submission_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        submission_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        submission_list = paginator.page(paginator.num_pages)
    print submission_list
    return render(request, template,{'submissions':submission_list})


def create_project(request, template="create_project.html"):
    form = ProjectForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        new_project = form.save()
        print new_project
        return  redirect('enterprise.projects')
    context = {"form": form, "title": _("Create Project")}
    return render(request, template, context)
