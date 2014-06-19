from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Submission(models.Model):
    grade = models.SmallIntegerField(verbose_name=_("grade"))
    project = models.CharField(verbose_name=_("project"),max_length='256')
    date = models.DateTimeField(verbose_name=_("date"))

    class Meta:
        verbose_name = _("Submission")
        ordering = ['date']

    def __str__(self):
        return 'Project:{}'.format(self.project)
