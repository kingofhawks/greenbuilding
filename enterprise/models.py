from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Project(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(verbose_name=_("project_name"),max_length=256)
    location = models.CharField(verbose_name=_("location"),max_length=256,blank=True)
    description = models.CharField(verbose_name=_("description"),max_length=1024,blank=True)
    construct_company = models.CharField(verbose_name=_('construct_company'),max_length=256, blank=True)
    contact = models.CharField(verbose_name=_('contact'),max_length=128, blank=True)
    phone = models.CharField(verbose_name=_('phone'),max_length=30, blank=True)
    address = models.CharField(verbose_name=_('address'),max_length=256, blank=True)
    zipcode = models.CharField(verbose_name=_('zipcode'),max_length=6, blank=True)

    class Meta:
        verbose_name = _("project")
        ordering = ['name']

    def __str__(self):
        return 'Project:{}'.format(self.name)


class Submission(models.Model):
    grade = models.SmallIntegerField(verbose_name=_("grade"))
    project = models.ForeignKey('Project')
    date = models.DateTimeField(verbose_name=_("date"))

    class Meta:
        verbose_name = _("submission")
        ordering = ['date']

    def __str__(self):
        return 'Project:{}'.format(self.project.name)


#Project application review form
class ApplicationReview(models.Model):
    project = models.ForeignKey('Project')
    grade = models.SmallIntegerField(verbose_name=_("grade"))
    date = models.DateTimeField(verbose_name=_("date"))

    class Meta:
        verbose_name = _("application_review")
        ordering = ['date']

    def __str__(self):
        return 'ApplicationReview:{}'.format(self.project.name)


class SelfEvaluation(models.Model):
    project = models.ForeignKey('Project')
    completion_date = models.DateTimeField(verbose_name=_("completion_date"))
    awards = models.CharField(verbose_name=_('awards'),max_length=256,blank=True)

    class Meta:
        verbose_name = _("self_evaluation")

    def __str__(self):
        return 'SelfEvaluation:{}'.format(self.project.name)


class Selection(models.Model):
    project = models.ForeignKey('Project')
    grade = models.SmallIntegerField(verbose_name=_("grade"))
    passed = models.BooleanField(verbose_name=_('passed'))

    class Meta:
        verbose_name = _("selection")

    def __str__(self):
        return 'Selection:{}'.format(self.project.name)


