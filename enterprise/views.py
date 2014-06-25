from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from models import Submission,Project,ApplicationReview,SelfEvaluation,Selection, PM10
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from forms import ProjectForm
from django.utils.translation import ugettext as _
import json
from django.http import HttpResponse


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


def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    print project
    return render(request, 'project_detail.html',{'project':project})


def project_submission(request, project_id):
    submission = get_object_or_404(Submission, project_id=project_id)
    print submission
    return render(request, 'project_submission.html',{'submission':submission})


def project_review(request, project_id):
    submission = get_object_or_404(Submission, project_id=project_id)
    print submission
    return render(request, 'project_submission.html',{'submission':submission})


def project_evaluation(request, project_id):
    submission = get_object_or_404(Submission, project_id=project_id)
    print submission
    return render(request, 'project_submission.html',{'submission':submission})


def project_monitor(request, project_id):
    submission = get_object_or_404(Submission, project_id=project_id)
    print submission
    return render(request, 'project_submission.html',{'submission':submission})


def project_selection(request, project_id):
    submission = get_object_or_404(Submission, project_id=project_id)
    print submission
    return render(request, 'project_submission.html',{'submission':submission})


def project_pm10(request, project_id):

    return render_to_response( 'project_pm10.html',{'project_id':project_id})


def pm10_data(request, project_id):
    query_set = PM10.objects.filter(project_id=project_id)
    pm10_list = []

    for pm10 in query_set:
        pm10_list.append({'date':pm10.date.date(),'value': pm10.value})

    #json.dumps do not work with DateTime object type,need to use DjangoJSONEncoder

    from django.core.serializers.json import DjangoJSONEncoder
    return HttpResponse(json.dumps(pm10_list, cls=DjangoJSONEncoder), content_type="application/json")
