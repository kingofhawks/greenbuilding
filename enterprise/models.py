from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from datetime import datetime
from django.core.urlresolvers import reverse


# Create your models here.
class Project(models.Model):
    user = models.ForeignKey(User)

    #project info
    name = models.CharField(verbose_name=_("project_name"), max_length=256)
    location = models.CharField(verbose_name=_("location"), max_length=256, blank=True, null=True)
    area = models.IntegerField(verbose_name=_('area'), blank=True, null=True)
    cost = models.IntegerField(verbose_name=_('cost'), blank=True, null=True)
    structure_type = models.CharField(verbose_name=_('structure_type'), max_length=32, blank=True, null=True)
    start_date = models.DateField(verbose_name=_('start_date'), blank=True, null=True)
    end_date = models.DateField(verbose_name=_('end_date'), blank=True, null=True)
    description = models.CharField(verbose_name=_("description"),max_length=1024,blank=True, null=True)

    #company info
    construct_company = models.CharField(verbose_name=_('construct_company'), max_length=256, blank=True, null=True)
    postal_address = models.CharField(verbose_name=_('postal_address'), max_length=256, blank=True, null=True)
    zipcode = models.CharField(verbose_name=_('zipcode'), max_length=6, blank=True, null=True)

    class Meta:
        verbose_name = _("project")
        ordering = ['name']

    def __str__(self):
        return 'Project:{}'.format(self.name)


class Submission(models.Model):
    grade = models.SmallIntegerField(verbose_name=_("grade"))
    project = models.ForeignKey(Project)
    date = models.DateTimeField(verbose_name=_("date"))
    person_in_charge = models.CharField(verbose_name=_('person_in_charge'), max_length=32, blank=True, null=True)
    phone1 = models.CharField(verbose_name=_('phone1'), max_length=32, blank=True, null=True)
    technical_in_charge = models.CharField(verbose_name=_('technical_in_charge'), max_length=32, blank=True, null=True)
    phone2 = models.CharField(verbose_name=_('phone2'), max_length=32, blank=True, null=True)
    company_technical_in_charge = models.CharField(verbose_name=_('company_technical_in_charge'), max_length=32, blank=True, null=True)
    phone3 = models.CharField(verbose_name=_('phone3'), max_length=32, blank=True, null=True)
    content = models.CharField(verbose_name=_('content'), max_length= 2048, blank=True, null=True)
    measures = models.CharField(verbose_name=_('measures'), max_length=1024, blank=True, null=True)
    schedule = models.CharField(verbose_name=_('schedule'), max_length=1024, blank=True, null=True)
    benefits = models.CharField(verbose_name=_('benefits'), max_length=1024, blank=True, null=True)
    company_opinion = models.CharField(verbose_name=_('company_opinion'), max_length=2048, blank=True, null=True)
    management_opinion = models.CharField(verbose_name=_('management_opinion'), max_length=2048, blank=True, null=True)
    approved = models.BooleanField(verbose_name=_('approved'), default=False)

    class Meta:
        verbose_name = _("submission")
        ordering = ['date']

    def __str__(self):
        return 'Submission:{}'.format(self.project.name)

    def get_absolute_url(self):
        return reverse('enterprise.project.submission', args=[str(self.id)])


#Project application review form
class ApplicationReview(models.Model):
    project = models.ForeignKey(Project)
    grade = models.SmallIntegerField(verbose_name=_("grade"))
    date = models.DateTimeField(verbose_name=_("date"))
    achievement = models.FileField(verbose_name=_('achievement'), upload_to='video', blank=True, null=True)
    contact = models.CharField(verbose_name=_('contact'), max_length=32, blank=True, null=True)
    phone = models.CharField(verbose_name=_('phone'), max_length=32, blank=True, null=True)
    content = models.CharField(verbose_name=_('content'), max_length=2048, blank=True, null=True)
    company_opinion = models.CharField(verbose_name=_('company_opinion'), max_length=2048, blank=True, null=True)
    management_opinion = models.CharField(verbose_name=_('management_opinion'), max_length=2048, blank=True, null=True)
    approved = models.BooleanField(verbose_name=_('approved'), default=False)

    class Meta:
        verbose_name = _("application_review")
        ordering = ['date']

    def __str__(self):
        return 'ApplicationReview:{}'.format(self.project.name)


class SelfEvaluation(models.Model):
    project = models.ForeignKey(Project)
    completion_date = models.DateTimeField(verbose_name=_("completion_date"))
    awards = models.CharField(verbose_name=_('awards'), max_length=256, blank=True, null=True)

    class Meta:
        verbose_name = _("self_evaluation")

    def __str__(self):
        return 'SelfEvaluation:{}'.format(self.project.name)


class ProgressMonitor(models.Model):
    project = models.ForeignKey(Project)
    date = models.DateTimeField(verbose_name=_("date"))
    pm10_threshold = models.IntegerField(verbose_name=_('pm10_threshold'))

    class Meta:
        verbose_name = _("progress_monitor")


class Selection(models.Model):
    project = models.ForeignKey(Project)
    grade = models.SmallIntegerField(verbose_name=_("grade"))
    passed = models.BooleanField(verbose_name=_('passed'), default=False)
    user = models.ForeignKey(User)

    class Meta:
        verbose_name = _("selection")

    def __str__(self):
        return 'Selection:{}'.format(self.project.name)


class PM10(models.Model):
    project = models.ForeignKey('Project')
    value = models.SmallIntegerField(verbose_name=_('value'))
    date = models.DateTimeField(verbose_name=_('date'))

    class Meta:
        verbose_name = _('pm10')

    def __str__(self):
        return 'PM10:{}'.format(self.value)


class Notification(models.Model):
    label = models.CharField(verbose_name=_('label'), max_length=256)
    type = models.SmallIntegerField(verbose_name=_('type'))
    project_url = models.CharField(verbose_name=_('project_url'), max_length=128)
    processed = models.BooleanField(verbose_name=_('processed'), default=False)
    date = models.DateTimeField(verbose_name=_('date'), blank=True, null=True, default=datetime.utcnow())

    class Meta:
        verbose_name = _('notification')

    def __str__(self):
        return 'Notification:{}'.format(self.label)


