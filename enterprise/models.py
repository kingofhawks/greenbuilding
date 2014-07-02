from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Project(models.Model):
    user = models.ForeignKey(User)

    #project info
    name = models.CharField(verbose_name=_("project_name"), max_length=256)
    location = models.CharField(verbose_name=_("location"), max_length=256,blank=True)
    area = models.IntegerField(verbose_name=_('area'), blank=True)
    cost = models.IntegerField(verbose_name=_('cost'), blank=True)
    structure_type = models.CharField(verbose_name=_('structure_type'), max_length=32, blank=True)
    start_date = models.DateField(verbose_name=_('start_date'),blank=True)
    end_date = models.DateField(verbose_name=_('end_date'),blank=True)
    description = models.CharField(verbose_name=_("description"),max_length=1024,blank=True)

    #company info
    construct_company = models.CharField(verbose_name=_('construct_company'), max_length=256, blank=True)
    postal_address = models.CharField(verbose_name=_('postal_address'), max_length=256, blank=True)
    zipcode = models.CharField(verbose_name=_('zipcode'), max_length=6, blank=True)

    class Meta:
        verbose_name = _("project")
        ordering = ['name']

    def __str__(self):
        return 'Project:{}'.format(self.name)


class Submission(models.Model):
    grade = models.SmallIntegerField(verbose_name=_("grade"))
    project = models.ForeignKey(Project)
    date = models.DateTimeField(verbose_name=_("date"))
    person_in_charge = models.CharField(verbose_name=_('person_in_charge'), max_length=32, blank=True)
    phone1 = models.CharField(verbose_name=_('phone1'), max_length=32, blank=True)
    technical_in_charge = models.CharField(verbose_name=_('technical_in_charge'), max_length=32, blank=True)
    phone2 = models.CharField(verbose_name=_('phone2'), max_length=32, blank=True)
    company_technical_in_charge = models.CharField(verbose_name=_('company_technical_in_charge'), max_length=32, blank=True)
    phone3 = models.CharField(verbose_name=_('phone3'), max_length=32, blank=True)
    content = models.CharField(verbose_name=_('content'), max_length= 2048, blank=True)
    measures = models.CharField(verbose_name=_('measures'), max_length=1024, blank=True)
    schedule = models.CharField(verbose_name=_('schedule'), max_length=1024, blank=True)
    benefits = models.CharField(verbose_name=_('benefits'), max_length=1024, blank=True)
    company_opinion = models.CharField(verbose_name=_('company_opinion'), max_length=2048, blank=True)
    management_opinion = models.CharField(verbose_name=_('management_opinion'), max_length=2048, blank=True)
    approved = models.BooleanField(verbose_name=_('approved'), default=False)

    class Meta:
        verbose_name = _("submission")
        ordering = ['date']

    def __str__(self):
        return 'Submission:{}'.format(self.project.name)


#Project application review form
class ApplicationReview(models.Model):
    project = models.ForeignKey(Project)
    grade = models.SmallIntegerField(verbose_name=_("grade"))
    date = models.DateTimeField(verbose_name=_("date"))
    achievement = models.FileField(verbose_name=_('achievement'), upload_to='video', blank=True)
    contact = models.CharField(verbose_name=_('contact'), max_length=32, blank=True)
    phone = models.CharField(verbose_name=_('phone'), max_length=32, blank=True)
    content = models.CharField(verbose_name=_('content'), max_length=2048, blank=True)
    company_opinion = models.CharField(verbose_name=_('company_opinion'), max_length=2048, blank=True)
    management_opinion = models.CharField(verbose_name=_('management_opinion'), max_length=2048, blank=True)
    approved = models.BooleanField(verbose_name=_('approved'), default=False)

    class Meta:
        verbose_name = _("application_review")
        ordering = ['date']

    def __str__(self):
        return 'ApplicationReview:{}'.format(self.project.name)


class SelfEvaluation(models.Model):
    project = models.ForeignKey(Project)
    completion_date = models.DateTimeField(verbose_name=_("completion_date"))
    awards = models.CharField(verbose_name=_('awards'),max_length=256,blank=True)

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


