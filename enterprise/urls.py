from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    # Examples:
    url(r'^projects$', views.ProjectList.as_view(), name='enterprise.projects'),
    url(r'^submissions$', views.SubmissionList.as_view(), name='enterprise.submissions'),
    url(r'^reviews$', views.ApplicationReviewList.as_view(), name='enterprise.reviews'),
    url(r'^evaluations', views.SelfEvaluationList.as_view(), name='enterprise.evaluations'),
    url(r'^selections', views.SelectionList.as_view(), name='enterprise.selections'),
    url(r'^notifications', views.NotificationList.as_view(), name='enterprise.notifications'),
    url(r'^notification/data/$', views.notification_data, name='enterprise.notification_data'),
    url(r'^project/add/$', views.create_project, name='enterprise.project.add'),
    url(r'^project/delete/$', views.delete_project, name='enterprise.project.delete'),
    url(r'^project/(?P<pk>\d+)/$', views.ProjectUpdate.as_view(), name='enterprise.project.update'),
    url(r'^projects/(?P<project_id>\d+)/$', views.project_detail, name='enterprise.project.detail'),
    url(r'^projects/(?P<project_id>\d+)/progress/$', views.project_progress, name='enterprise.project.progress'),
    url(r'^projects/(?P<project_id>\d+)/submission/$', views.project_submission, name='enterprise.project.submission'),
    url(r'^projects/(?P<project_id>\d+)/submission/preview/$', views.project_submission_preview, name='enterprise.project.submission.preview'),
    url(r'^projects/(?P<project_id>\d+)/submission/pdf/$', views.project_submission_pdf, name='enterprise.project.submission.pdf'),
    url(r'^submissions/commit/$', views.submission_commit, name='enterprise.submission.commit'),
    url(r'^submissions/approve/$', views.submission_approve, name='enterprise.submission.approve'),
    url(r'^submissions/deny/$', views.submission_deny, name='enterprise.submission.deny'),
    url(r'^submission/add/$', views.create_submission, name='enterprise.submission.add'),
    url(r'^projects/(?P<project_id>\d+)/review/$', views.project_review, name='enterprise.project.review'),
    url(r'^projects/(?P<project_id>\d+)/review/pdf/$', views.project_review_pdf, name='enterprise.project.review.pdf'),
    url(r'^reviews/commit/$', views.review_commit, name='enterprise.review.commit'),
    url(r'^review/add/$', views.create_review, name='enterprise.review.add'),
    url(r'^review/(?P<project_id>\d+)/approve/$', views.review_approve, name='enterprise.review.approve'),
    url(r'^review/(?P<project_id>\d+)/deny/$', views.review_deny, name='enterprise.review.deny'),
    url(r'^review/(?P<project_id>\d+)/summary/$', views.review_summary, name='enterprise.review.summary'),
    url(r'^review/(?P<project_id>\d+)/photo/$', views.review_photo, name='enterprise.review.photo'),
    url(r'^project/(?P<project_id>\d+)/achievement/$', views.project_achievement, name='enterprise.project.achievement'),
    url(r'^project/(?P<project_id>\d+)/summary/$', views.project_summary_report, name='enterprise.project.summary'),
    url(r'^project/(?P<project_id>\d+)/presentation/$', views.project_presentation, name='enterprise.project.presentation'),
    url(r'^project/(?P<project_id>\d+)/pdf/element$', views.element_evaluation_pdf, name='enterprise.project.pdf.element'),
    url(r'^project/(?P<project_id>\d+)/pdf/batch$', views.batch_evaluation_pdf, name='enterprise.project.pdf.batch'),
    url(r'^project/(?P<project_id>\d+)/pdf/stage$', views.stage_evaluation_pdf, name='enterprise.project.pdf.stage'),
    url(r'^project/(?P<project_id>\d+)/pdf/unit$', views.unit_evaluation_pdf, name='enterprise.project.pdf.unit'),
    url(r'^project/(?P<project_id>\d+)/form$', views.project_evaluation_form, name='enterprise.project.form'),
    url(r'^project/(?P<project_id>\d+)/print/element/$', views.element_evaluation_print, name='enterprise.project.print.element'),
    url(r'^project/(?P<project_id>\d+)/print/batch/$', views.batch_evaluation_print, name='enterprise.project.print.batch'),
    url(r'^project/(?P<project_id>\d+)/print/stage/$', views.stage_evaluation_print, name='enterprise.project.print.stage'),
    url(r'^project/(?P<project_id>\d+)/print/unit/$', views.unit_evaluation_print, name='enterprise.project.print.unit'),
    url(r'^projects/(?P<project_id>\d+)/evaluation/$', views.project_evaluation, name='enterprise.project.evaluation'),
    url(r'^projects/(?P<project_id>\d+)/element/add/$', views.create_element_evaluation_form, name='enterprise.project.element.add'),
    url(r'^projects/(?P<project_id>\d+)/batch/add/$', views.create_batch_evaluation_form, name='enterprise.project.batch.add'),
    url(r'^projects/(?P<project_id>\d+)/stage/add/$', views.create_stage_evaluation_form, name='enterprise.project.stage.add'),
    url(r'^projects/(?P<project_id>\d+)/unit/add/$', views.create_unit_evaluation_form, name='enterprise.project.unit.add'),
    url(r'^projects/(?P<project_id>\d+)/monitor/$', views.project_monitor, name='enterprise.project.monitor'),
    url(r'^projects/(?P<project_id>\d+)/selection/$', views.project_selection, name='enterprise.project.selection'),
    url(r'^projects/(?P<project_id>\d+)/pm10/$', views.project_pm10, name='enterprise.project.pm10'),
    url(r'^projects/(?P<project_id>\d+)/pm10/data/$', views.pm10_data, name='enterprise.project.pm10_data'),
    url(r'^projects/(?P<project_id>\d+)/noise/$', views.project_noise, name='enterprise.project.noise'),
)


