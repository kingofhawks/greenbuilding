from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'worksmart.views.home', name='home'),
    #url(r'^$', views.trend, name='trend'),
    #url(r'^list/new/$', views.new_list, name='enterprise.list.new'),
    url(r'^projects$', views.ProjectList.as_view(), name='enterprise.projects'),
    url(r'^submissions$', views.SubmissionList.as_view(), name='enterprise.applications'),
    url(r'^reviews', views.ApplicationReviewList.as_view(), name='enterprise.reviews'),
    url(r'^evaluations', views.SelfEvaluationList.as_view(), name='enterprise.evaluations'),
    url(r'^selections', views.SelectionList.as_view(), name='enterprise.selections'),
    url(r'^project/add/$', views.create_project, name='enterprise.project.add'),

)
