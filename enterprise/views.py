from django.shortcuts import render, redirect, get_object_or_404, render_to_response, get_list_or_404
from models import Submission, Project, ApplicationReview, SelfEvaluation, Selection, PM10, ProgressMonitor, Notification
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from forms import ProjectForm
from django.utils.translation import ugettext as _
import json
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.messages import info


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


class NotificationList(ListView):
    model = Notification
    template_name = 'notification_list.html'
    context_object_name = 'notifications'

    def get_queryset(self):
        return Notification.objects.filter(processed=False)


# Create your views here.
def new_list(request, template="submission_list.html"):
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


def delete_project(request, template="create_project.html"):
    form = ProjectForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        new_project = form.save()
        print new_project
        return  redirect('enterprise.projects')
    context = {"form": form, "title": _("Create Project")}
    return render(request, template, context)


@login_required
def project_detail(request, project_id):
    print request.user.is_authenticated()
    print 'session*************'
    print request.session
    project = get_object_or_404(Project, pk=project_id)
    print project
    return render(request, 'project_detail.html',{'project':project, 'project_id':project_id})


def project_progress(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    print project
    return render(request, 'project_progress.html',{'project':project, 'project_id':project_id})


@login_required
def project_submission(request, project_id):
    submission = get_object_or_404(Submission, project_id=project_id)
    print submission
    return render(request, 'project_submission.html', {'submission': submission, 'project_id': project_id})


def project_submission_preview(request, project_id):
    submission = get_object_or_404(Submission, project_id=project_id)
    print submission
    return render(request, 'project_submission_preview.html', {'submission': submission, 'project_id': project_id})


def project_submission_pdf(request, project_id):
    submission = get_object_or_404(Submission, project_id=project_id)
    print submission
    return render(request, 'project_submission_pdf.html', {'submission': submission, 'project_id': project_id})


def submission_commit(request):
    project_id = request.POST.get('project_id')
    print project_id
    submission = get_object_or_404(Submission, pk=project_id)
    project = submission.project.name
    n = Notification(label=project, type=1, project_url=submission.get_absolute_url());
    n.save();

    return HttpResponse(json.dumps('OK'), content_type="application/json")


def submission_approve(request):
    project_id = request.POST.get('project_id')
    print project_id
    #update submission status
    submission = get_object_or_404(Submission, pk=project_id)
    print submission
    submission.approved = True
    submission.save()

    #clear relevant notification
    notification = get_object_or_404(Notification, label=submission.project.name)
    print notification
    notification.delete()
    info(request, _("Submission approved"))

    #generate PDF
    from tasks import html2pdf
    html2pdf('E:/workspace/greenbuilding/media/submission/', project_id)

    return HttpResponse(json.dumps('OK'), content_type="application/json")


def submission_deny(request):
    project_id = request.POST.get('project_id')
    print project_id
    submission = get_object_or_404(Submission, pk=project_id)
    submission.approved = False
    submission.save();

    notification = get_object_or_404(Notification, project=submission.project.name)
    notification.delete()
    info(request, _("Submission denied"))

    return HttpResponse(json.dumps('OK'), content_type="application/json")


@login_required
def project_review(request, project_id):
    review = get_object_or_404(ApplicationReview, project_id=project_id)
    print review
    return render(request, 'project_review.html',{'review':review, 'project_id':project_id})


def project_review_pdf(request, project_id):
    review = get_object_or_404(ApplicationReview, project_id=project_id)
    print review
    return render(request, 'project_review_pdf.html', {'review': review, 'project_id': project_id})


def review_commit(request):
    project_id = request.POST.get('project_id')
    print project_id
    review = get_object_or_404(ApplicationReview, pk=project_id)
    project = review.project.name
    n = Notification(label=project, type=2, project_url=review.get_absolute_url());
    n.save();

    return HttpResponse(json.dumps('OK'), content_type="application/json")


@login_required
def project_evaluation(request, project_id):
    evaluation = get_object_or_404(SelfEvaluation, project_id=project_id)
    print evaluation
    return render(request, 'project_evaluation.html',{'evaluation':evaluation, 'project_id':project_id})


@login_required
def project_monitor(request, project_id):
    monitor = get_object_or_404(ProgressMonitor, project_id=project_id)
    print monitor
    return render(request, 'project_monitor.html',{'monitor':monitor, 'project_id':project_id})


@login_required
def project_selection(request, project_id):
    selections = Selection.objects.filter(project_id=project_id)
    print selections
    return render(request, 'project_selection.html',{'selections':selections, 'project_id':project_id})


@login_required
def project_pm10(request, project_id):

    return render_to_response( 'project_pm10.html',{'project_id':project_id})


@login_required
def pm10_data(request, project_id):
    query_set = PM10.objects.filter(project_id=project_id)
    pm10_list = []

    for pm10 in query_set:
        pm10_list.append({'date':pm10.date.date(),'value': pm10.value})

    #json.dumps do not work with DateTime object type,need to use DjangoJSONEncoder
    from django.core.serializers.json import DjangoJSONEncoder
    return HttpResponse(json.dumps(pm10_list, cls=DjangoJSONEncoder), content_type="application/json")


@login_required
def project_noise(request, project_id):

    return render_to_response( 'project_pm10.html',{'project_id':project_id})


def notification_data(request):
    from django.core import serializers
    query_set = Notification.objects.filter(processed=False)
    data = serializers.serialize("json", query_set)

    return HttpResponse(data, content_type="application/json")
