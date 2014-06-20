from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'worksmart.views.home', name='home'),
    #url(r'^$', views.trend, name='trend'),
    #url(r'^list/new/$', views.new_list, name='enterprise.list.new'),
    url(r'^submissions$', views.SubmissionList.as_view(), name='enterprise.applications'),
    url(r'^projects$', views.ProjectList.as_view(), name='enterprise.projects'),
)
