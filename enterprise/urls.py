from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    # Examples:
    url(r'^projects$', views.ProjectList.as_view(), name='enterprise.projects'),
    url(r'^submissions$', views.SubmissionList.as_view(), name='enterprise.applications'),
    url(r'^reviews', views.ApplicationReviewList.as_view(), name='enterprise.reviews'),
    url(r'^evaluations', views.SelfEvaluationList.as_view(), name='enterprise.evaluations'),
    url(r'^selections', views.SelectionList.as_view(), name='enterprise.selections'),
    url(r'^notifications', views.NotificationList.as_view(), name='enterprise.notifications'),
    url(r'^notification/data/$', views.notification_data, name='enterprise.notification_data'),
    url(r'^project/add/$', views.create_project, name='enterprise.project.add'),
    url(r'^projects/(?P<project_id>\d+)/$', views.project_detail, name='enterprise.project.detail'),
    url(r'^projects/(?P<project_id>\d+)/submission/$', views.project_submission, name='enterprise.project.submission'),
    url(r'^submissions/commit/$', views.submission_commit, name='enterprise.submission.commit'),
    url(r'^projects/(?P<project_id>\d+)/review/$', views.project_review, name='enterprise.project.review'),
    url(r'^projects/(?P<project_id>\d+)/evaluation/$', views.project_evaluation, name='enterprise.project.evaluation'),
    url(r'^projects/(?P<project_id>\d+)/monitor/$', views.project_monitor, name='enterprise.project.monitor'),
    url(r'^projects/(?P<project_id>\d+)/selection/$', views.project_selection, name='enterprise.project.selection'),
    url(r'^projects/(?P<project_id>\d+)/pm10/$', views.project_pm10, name='enterprise.project.pm10'),
    url(r'^projects/(?P<project_id>\d+)/pm10/data/$', views.pm10_data, name='enterprise.project.pm10_data'),
    url(r'^projects/(?P<project_id>\d+)/noise/$', views.project_noise, name='enterprise.project.noise'),
)


