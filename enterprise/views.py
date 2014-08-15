from django.shortcuts import render, redirect, get_object_or_404, render_to_response, get_list_or_404
from models import (Submission, Project, ApplicationReview, SelfEvaluation, Selection, PM10, ProgressMonitor,
                    Notification, Picture, ElementEvaluationForm, BatchEvaluationForm, StageEvaluationForm,
                    UnitEvaluationForm)
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from forms import (ProjectForm, SubmissionForm, ReviewForm, ElementEvaluationFormForm, BatchEvaluationFormForm,
                   StageEvaluationFormForm, UnitEvaluationFormForm)
from django.utils.translation import ugettext as _
import json
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.messages import info, warning
from tasks import html2pdf
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe
from django.core import serializers
#json.dumps do not work with DateTime object type,need to use DjangoJSONEncoder
from django.core.serializers.json import DjangoJSONEncoder


class ProjectList(ListView):
    model = Project
    template_name = 'project_list.html'
    context_object_name = 'projects'


class ProjectUpdate(UpdateView):
    model = Project
    template_name = 'create_project.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ProjectUpdate, self).get_context_data(**kwargs)
        # Add extra context variable
        context['title'] = _('Modify Project')
        return context


class SubmissionList(ListView):
    model = Submission
    template_name = 'submission_list.html'
    context_object_name = 'projects'


class SubmissionUpdate(UpdateView):
    model = Submission
    template_name = 'create_project.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(SubmissionUpdate, self).get_context_data(**kwargs)
        # Add extra context variable
        context['title'] = _('Modify Submission')
        return context


class ApplicationReviewList(ListView):
    model = ApplicationReview
    template_name = 'review_list.html'
    context_object_name = 'projects'


class ApplicationReviewUpdate(UpdateView):
    model = ApplicationReview
    template_name = 'create_project.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ApplicationReviewUpdate, self).get_context_data(**kwargs)
        # Add extra context variable
        context['title'] = _('Modify ApplicationReview')
        return context


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
    return render(request, template, {'submissions': submission_list})


def create_project(request, template="create_project.html"):
    form = ProjectForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        new_project = form.save()
        print new_project
        return redirect('enterprise.projects')
    context = {"form": form, "title": _("Create Project")}
    return render(request, template, context)


def delete_project(request, template="create_project.html"):
    form = ProjectForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        new_project = form.save()
        print new_project
        return redirect('enterprise.projects')
    context = {"form": form, "title": _("Create Project")}
    return render(request, template, context)


@login_required
def project_detail(request, project_id):
    print request.user.is_authenticated()
    print 'session*************'
    print request.session.keys()
    print request.session['_auth_user_id']
    project = get_object_or_404(Project, pk=project_id)
    print project
    return render(request, 'project_detail.html', {'project': project, 'project_id': project_id})


def project_progress(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    print project
    return render(request, 'project_progress.html', {'project': project, 'project_id': project_id})


@login_required
def project_submission(request, project_id):
    submission = None
    try:
        submission = get_object_or_404(Submission, project_id=project_id)
        print submission
    except Http404:
        url = reverse('enterprise.submission.add')
        #unicode to gb2312
        msg = (_("Submission is not submitted yet.") + "<a target='_blank' href='{}'>".format(url)
               + _('New Submission')+"</a>").encode('gb2312')
        print msg
        #mark_safe will show raw HTML, rather than escape HTML tags
        warning(request, mark_safe(_("Submission is not submitted yet.")+"<a target='_blank' href={}> Create </a>".format(url)))
    return render(request, 'project_submission.html', {'submission': submission, 'project_id': project_id})


def project_submission_preview(request, project_id):
    submission = get_object_or_404(Submission, project_id=project_id)
    print submission
    return render(request, 'project_submission_preview.html', {'submission': submission, 'project_id': project_id})


def project_submission_pdf(request, project_id):
    submission = get_object_or_404(Submission, project_id=project_id)
    print submission
    return render(request, 'project_submission_pdf.html', {'submission': submission, 'project_id': project_id})


def create_submission(request, template="create_project.html"):
    form = SubmissionForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        new_project = form.save()
        print new_project
        return redirect('enterprise.submissions')
    context = {"form": form, "title": _("Create Submission")}
    return render(request, template, context)


def submission_commit(request):
    project_id = request.POST.get('project_id')
    print project_id
    submission = get_object_or_404(Submission, pk=project_id)
    project = submission.project.name

    messages = 'OK'
    try:
        notification = get_object_or_404(Notification, label=project, type=1)
        print notification
        messages = _('Submission already committed.')
    except Http404:
        n = Notification(label=project, type=1, project_url=submission.get_absolute_url());
        n.save();

    return HttpResponse(json.dumps(messages), content_type="application/json")


def submission_approve(request):
    project_id = request.POST.get('project_id')
    print project_id
    #update submission status
    submission = get_object_or_404(Submission, pk=project_id)
    print submission
    submission.approved = True
    submission.save()

    #clear relevant notification
    try:
        notification = get_object_or_404(Notification, label=submission.project.name, type=1)
        print notification
        notification.delete()
    except Http404:
        pass
    info(request, _("Submission approved"))

    #generate PDF
    html2pdf(request.build_absolute_uri(submission.get_pdf_url()), 'E:/workspace/greenbuilding/media/submission/', project_id)

    return HttpResponse(json.dumps('OK'), content_type="application/json")


def submission_deny(request):
    project_id = request.POST.get('project_id')
    print project_id
    submission = get_object_or_404(Submission, pk=project_id)
    submission.approved = False
    submission.save();

    try:
        notification = get_object_or_404(Notification, label=submission.project.name, type=1)
        notification.delete()
    except Http404:
        pass

    info(request, _("Submission denied"))

    return HttpResponse(json.dumps('OK'), content_type="application/json")


@login_required
def project_review(request, project_id):
    review = None
    try:
        review = get_object_or_404(ApplicationReview, project_id=project_id)
        print review
    except Http404:
        url = reverse('enterprise.review.add')
        warning(request, mark_safe(_("Review is not submitted yet.")+"<a target='_blank' href={}> Create </a>".format(url)))
        review = ApplicationReview(id=99999)#hack an empty review
    return render(request, 'project_review.html', {'review': review, 'project_id': project_id})


def project_review_pdf(request, project_id):
    review = get_object_or_404(ApplicationReview, project_id=project_id)
    print review
    return render(request, 'project_review_pdf.html', {'review': review, 'project_id': project_id})


def create_review(request, template="create_project.html"):
    #form = ReviewForm(request.POST or None)
    if request.method == "POST":
        #Must pass request.FILES to ModelForm so it can handle file upload
        form = ReviewForm(request.POST, request.FILES)
        new_project = form.save()
        print new_project
        return redirect('enterprise.reviews')
    else:
        form = ReviewForm()
    context = {"form": form, "title": _("Create ApplicationReview")}
    return render(request, template, context)


def review_commit(request):
    project_id = request.POST.get('project_id')
    print project_id
    review = get_object_or_404(ApplicationReview, pk=project_id)
    project = review.project.name

    messages = 'OK'
    try:
        notification = get_object_or_404(Notification, label=project, type=2)
        print notification
        messages = _('ApplicationReview already committed.')
    except Http404:
        n = Notification(label=project, type=2, project_url=review.get_absolute_url());
        n.save();

    return HttpResponse(json.dumps(messages), content_type="application/json")


def review_approve(request, project_id):
    #project_id = request.POST.get('project_id')
    print project_id
    #update review status
    review = get_object_or_404(ApplicationReview, pk=project_id)
    print review
    review.approved = True
    review.save()

    try:
    #clear relevant notification
        notification = get_object_or_404(Notification, label=review.project.name, type=2)
        notification.delete()
    except Http404:
        pass
    info(request, _("ApplicatonReview approved"))

    #generate PDF
    html2pdf(request.build_absolute_uri(review.get_pdf_url()), 'E:/workspace/greenbuilding/media/review/', project_id)

    return HttpResponse(json.dumps('OK'), content_type="application/json")


def review_deny(request, project_id):
    #project_id = request.POST.get('project_id')
    print project_id
    review = get_object_or_404(ApplicationReview, pk=project_id)
    review.approved = False
    review.save();

    try:
        notification = get_object_or_404(Notification, label=review.project.name, type=1)
        notification.delete()
    except Http404:
        pass
    info(request, _("ApplicatonReview denied"))

    return HttpResponse(json.dumps('OK'), content_type="application/json")


def project_summary_report(request, project_id):
    review = None
    try:
        review = get_object_or_404(ApplicationReview, project_id=project_id)
        print review
    except Http404:
        warning(request, _('Review is not submitted yet.'))
        review = ApplicationReview(id=99999)#hack an empty review
    return render(request, 'project_summary_report.html', {'review': review, 'project_id': project_id})


def project_presentation(request, project_id):
    review = None
    try:
        review = get_object_or_404(ApplicationReview, project_id=project_id)
        print review
    except Http404:
        warning(request, _('Review is not submitted yet.'))
        review = ApplicationReview(id=99999)#hack an empty review
    return render(request, 'project_presentation.html', {'review': review, 'project_id': project_id})


def review_summary(request, project_id):
    print project_id
    field_id = request.POST.get('field_id')
    field_content = request.POST.get('field_content')
    #print 'field_id:{} field_content:{}'.format(field_id,field_content)
    from django.db import connection
    cursor = connection.cursor()

    cursor.execute("UPDATE enterprise_ApplicationReview SET {}".format(field_id)+" = %s WHERE id = %s", [field_content, project_id])

    return HttpResponse(json.dumps('OK'), content_type="application/json")


def review_photo(request, project_id):
    print project_id
    review = None
    try:
        review = get_object_or_404(ApplicationReview, pk=project_id)
        print review
    except Http404:
        warning(request, _('Review is not submitted yet.'))
        review = ApplicationReview(id=99999)#hack an empty review

    print request.FILES
    picture = Picture(review=review, file=request.FILES['files'])
    picture.save()

    return HttpResponse(json.dumps('OK'), content_type="application/json")


def project_achievement(request, project_id):
    review = None
    try:
        review = get_object_or_404(ApplicationReview, project_id=project_id)
        print review
    except Http404:
        warning(request, _('Review is not submitted yet.'))
        review = ApplicationReview(id=99999)#hack an empty review

    pictures = None
    try:
        pictures = get_list_or_404(Picture, review=review)
        print pictures
    except Http404:
        warning(request, _('Pictures is not uploaded yet.'))

    return render(request, 'project_achievement.html', {'review': review, 'project_id': project_id, 'pictures': pictures})


def project_achievement_pictures(request, project_id):
    pictures = None
    try:
        pictures = get_list_or_404(Picture, review_id=project_id)
        print pictures
    except Http404:
        pass

    result = []
    if pictures is not None:
        for picture in pictures:
            #print picture
            #print picture.file
            #print picture.file.url
            result.append(picture.file.url)

    return HttpResponse(json.dumps(result), content_type="application/json")


def element_evaluation_pdf(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    print project
    form = get_object_or_404(ElementEvaluationForm, project_id=project_id)
    print form
    return render(request, 'element_evaluation_pdf.html', {'form': form, 'project': project,  'project_id': project_id})


def batch_evaluation_pdf(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    print project
    form = get_object_or_404(BatchEvaluationForm, project_id=project_id)
    print form
    return render(request, 'batch_evaluation_pdf.html', {'form': form,  'project': project, 'project_id': project_id})


def stage_evaluation_pdf(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    print project
    form = get_object_or_404(StageEvaluationForm, project_id=project_id)
    print form
    return render(request, 'stage_evaluation_pdf.html', {'form': form,  'project': project, 'project_id': project_id})


def unit_evaluation_pdf(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    print project
    form = get_object_or_404(UnitEvaluationForm, project_id=project_id)
    print form
    return render(request, 'unit_evaluation_pdf.html', {'form': form,  'project': project, 'project_id': project_id})


def project_evaluation_form(request, project_id):
    review = None
    try:
        review = get_object_or_404(ApplicationReview, project_id=project_id)
        print review
    except Http404:
        warning(request, _('Review is not submitted yet.'))
        review = ApplicationReview(id=99999)#hack an empty review

    return render(request, 'project_evaluation_form.html', {'review': review, 'project_id': project_id})


def element_evaluation_print(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    print project

    #generate PDF
    pdf_url = reverse('enterprise.project.pdf.element', args=[str(project_id)])
    html2pdf(request.build_absolute_uri(pdf_url), 'E:/workspace/greenbuilding/media/review/form/element/', project_id)

    return render(request, 'element_evaluation_print.html', {'project_id': project_id})


def create_element_evaluation_form(request, project_id, template="create_project.html"):
    form = ElementEvaluationFormForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        new_project = form.save()
        print new_project
        return redirect('enterprise.project.form', project_id=project_id)
    context = {"form": form, "title": _("Create Element Evaluation Form")}
    return render(request, template, context)


def batch_evaluation_print(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    print project

    #generate PDF
    pdf_url = reverse('enterprise.project.pdf.batch', args=[str(project_id)])
    html2pdf(request.build_absolute_uri(pdf_url), 'E:/workspace/greenbuilding/media/review/form/batch/', project_id)

    return render(request, 'batch_evaluation_print.html', {'project_id': project_id})


def create_batch_evaluation_form(request, project_id, template="create_project.html"):
    form = BatchEvaluationFormForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        new_project = form.save()
        print new_project
        return redirect('enterprise.project.form', project_id=project_id)
    context = {"form": form, "title": _("Create Batch Evaluation Form")}
    return render(request, template, context)


def stage_evaluation_print(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    print project

    #generate PDF
    pdf_url = reverse('enterprise.project.pdf.stage', args=[str(project_id)])
    html2pdf(request.build_absolute_uri(pdf_url), 'E:/workspace/greenbuilding/media/review/form/stage/', project_id)

    return render(request, 'stage_evaluation_print.html', {'project_id': project_id})


def create_stage_evaluation_form(request, project_id, template="create_project.html"):
    form = StageEvaluationFormForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        new_project = form.save()
        print new_project
        return redirect('enterprise.project.form', project_id=project_id)
    context = {"form": form, "title": _("Create Stage Evaluation Form")}
    return render(request, template, context)


def unit_evaluation_print(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    print project

    #generate PDF
    pdf_url = reverse('enterprise.project.pdf.unit', args=[str(project_id)])
    html2pdf(request.build_absolute_uri(pdf_url), 'E:/workspace/greenbuilding/media/review/form/unit/', project_id)

    return render(request, 'unit_evaluation_print.html', { 'project_id': project_id})


def create_unit_evaluation_form(request, project_id, template="create_project.html"):
    form = UnitEvaluationFormForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        new_project = form.save()
        print new_project
        return redirect('enterprise.project.form', project_id=project_id)
    context = {"form": form, "title": _("Create Unit Evaluation Form")}
    return render(request, template, context)


@login_required
def project_evaluation(request, project_id):
    evaluation = get_object_or_404(SelfEvaluation, project_id=project_id)
    print evaluation
    return render(request, 'project_evaluation.html', {'evaluation': evaluation, 'project_id': project_id})


@login_required
def project_monitor(request, project_id):
    monitor = get_object_or_404(ProgressMonitor, project_id=project_id)
    print monitor
    return render(request, 'project_monitor.html', {'monitor': monitor, 'project_id': project_id})


@login_required
def project_selection(request, project_id):
    from django.contrib.auth.models import User
    user = get_object_or_404(User, pk=request.user.pk)

    if request.method == "POST":
        print request.POST.get('user')
        thumbs_up = request.POST.get('thumbsUp')
        user_id = request.session['_auth_user_id']
        print user_id
        selection = Selection()

        selection.user = user
        project = get_object_or_404(Project, pk=project_id)
        selection.project = project
        if thumbs_up == 'true':
            selection.passed = True
        selection.save()

        query_set = Selection.objects.filter(pk=selection.id)
        data = serializers.serialize("json", query_set)
        print data
        return HttpResponse(data, content_type="application/json")
        #return HttpResponse(json.dumps(selection), content_type="application/json")
    else:
        selections = Selection.objects.filter(project_id=project_id)
        print selections
        print user.has_perm('enterprise.approve_submission')
        print user.has_perm('enterprise.add_submission')
        return render(request, 'project_selection.html', {'selections': selections, 'project_id': project_id})


@login_required
def project_pm10(request, project_id):

    return render_to_response('project_pm10.html', {'project_id':project_id})


@login_required
def pm10_data(request, project_id):
    query_set = PM10.objects.filter(project_id=project_id)
    pm10_list = []

    for pm10 in query_set:
        pm10_list.append({'date': pm10.date.date(), 'value': pm10.value})


    return HttpResponse(json.dumps(pm10_list, cls=DjangoJSONEncoder), content_type="application/json")


@login_required
def project_noise(request, project_id):

    return render_to_response('project_pm10.html', {'project_id': project_id})


def notification_data(request):
    query_set = Notification.objects.filter(processed=False)
    data = serializers.serialize("json", query_set)

    return HttpResponse(data, content_type="application/json")
