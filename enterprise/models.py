from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Project(models.Model):
    name = models.CharField(verbose_name=_("project_name"),max_length=256)
    location = models.CharField(verbose_name=_("location"),max_length=256)
    description = models.CharField(verbose_name=_("description"),max_length=1024)

    class Meta:
        verbose_name = _("Project")
        ordering = ['name']

    def __str__(self):
        return 'Project:{}'.format(self.name)


class Submission(models.Model):
    grade = models.SmallIntegerField(verbose_name=_("grade"))
    project = models.CharField(verbose_name=_("project"),max_length='256')
    date = models.DateTimeField(verbose_name=_("date"))

    class Meta:
        verbose_name = _("Submission")
        ordering = ['date']

    def __str__(self):
        return 'Project:{}'.format(self.project)
