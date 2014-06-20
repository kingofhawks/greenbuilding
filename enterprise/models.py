from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Project(models.Model):
    name = models.CharField(verbose_name=_("project_name"),max_length=256)
    location = models.CharField(verbose_name=_("location"),max_length=256,null=True)
    description = models.CharField(verbose_name=_("description"),max_length=1024,null=True)
    construct_company = models.CharField(verbose_name=_('construct_company'),max_length=256, null=True)
    contact = models.CharField(verbose_name=_('contact'),max_length=128, null=True)
    phone = models.CharField(verbose_name=_('phone'),max_length=30, null=True)
    address = models.CharField(verbose_name=_('address'),max_length=256, null=True)
    zipcode = models.CharField(verbose_name=_('zipcode'),max_length=6, null=True)

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
