from django.shortcuts import render
from models import Submission
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView


class SubmissionList(ListView):
    model = Submission
    template_name = 'submission_list.html'
    context_object_name = 'submissions'


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
