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
    description = models.CharField(verbose_name=_("description"), max_length=1024, blank=True, null=True)

    #company info
    construct_company = models.CharField(verbose_name=_('construct_company'), max_length=256, blank=True, null=True)
    postal_address = models.CharField(verbose_name=_('postal_address'), max_length=256, blank=True, null=True)
    zipcode = models.CharField(verbose_name=_('zipcode'), max_length=6, blank=True, null=True)

    class Meta:
        verbose_name = _("project")
        ordering = ['name']

    def __str__(self):
        return 'Project:{}'.format(self.name)

    def get_progress(self):
        return "3/5"

GRADE_CHOICES = (
        (_('green_building'), _('green_building')),
        (_('green_building_demo'), _('green_building_demo')),
)


class Submission(models.Model):
    grade = models.CharField(verbose_name=_("Grade"), max_length=64, choices=GRADE_CHOICES)
    project = models.ForeignKey(Project)
    date = models.DateTimeField(verbose_name=_("Date"), default=datetime.utcnow())
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
        return reverse('enterprise.project.submission', args=[str(self.project.id)])

    def get_pdf_url(self):
        return reverse('enterprise.project.submission.pdf', args=[str(self.project.id)])


#Project application review form
class ApplicationReview(models.Model):
    project = models.ForeignKey(Project)
    grade = models.CharField(verbose_name=_("Grade"), max_length=64, choices=GRADE_CHOICES)
    date = models.DateTimeField(verbose_name=_("Date"), default=datetime.utcnow())
    achievement = models.FileField(verbose_name=_('Achievement'), upload_to='video', blank=True, null=True)
    contact = models.CharField(verbose_name=_('contact'), max_length=32, blank=True, null=True)
    phone = models.CharField(verbose_name=_('phone'), max_length=32, blank=True, null=True)
    content = models.CharField(verbose_name=_('content'), max_length=2048, blank=True, null=True)
    company_opinion = models.CharField(verbose_name=_('company_opinion'), max_length=2048, blank=True, null=True)
    management_opinion = models.CharField(verbose_name=_('management_opinion'), max_length=2048, blank=True, null=True)
    approved = models.BooleanField(verbose_name=_('approved'), default=False)

    #summary report
    general = models.CharField(verbose_name=_('Project General'), max_length=2048, blank=True, null=True)
    characteristic = models.CharField(verbose_name=_('Project Characteristic'), max_length=2048, blank=True, null=True)
    construct_management = models.CharField(verbose_name=_('Construct Management'), max_length=2048, blank=True, null=True)
    env_protection_measure = models.CharField(verbose_name=_('Environment Protection Measure'), max_length=2048, blank=True, null=True)
    economize_materials = models.CharField(verbose_name=_('Economize on raw materials'), max_length=2048, blank=True, null=True)
    economize_waters = models.CharField(verbose_name=_('Economize on water'), max_length=2048, blank=True, null=True)
    economize_powers = models.CharField(verbose_name=_('Economize on power'), max_length=2048, blank=True, null=True)
    economize_land = models.CharField(verbose_name=_('Economize on land'), max_length=2048, blank=True, null=True)
    new_technology = models.CharField(verbose_name=_('New Technology'), max_length=2048, blank=True, null=True)
    new_equipment = models.CharField(verbose_name=_('New Equipment'), max_length=2048, blank=True, null=True)
    new_craft = models.CharField(verbose_name=_('New Materials and  Craft'), max_length=2048, blank=True, null=True)
    industrialization = models.CharField(verbose_name=_('Industrialization of construction industry'), max_length=2048, blank=True, null=True)
    comprehensive_benefit = models.CharField(verbose_name=_('Comprehensive Benefit'), max_length=2048, blank=True, null=True)

    class Meta:
        verbose_name = _("application_review")
        ordering = ['date']

    def __str__(self):
        return 'ApplicationReview:{}'.format(self.project.name)

    def get_absolute_url(self):
        return reverse('enterprise.project.review', args=[str(self.project.id)])

    def get_pdf_url(self):
        return reverse('enterprise.project.review.pdf', args=[str(self.project.id)])


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
    date = models.DateTimeField(verbose_name=_("Date"))
    pm10_threshold = models.IntegerField(verbose_name=_('pm10_threshold'))

    class Meta:
        verbose_name = _("progress_monitor")


class Selection(models.Model):
    user = models.ForeignKey(User)
    project = models.ForeignKey(Project)
    grade = models.SmallIntegerField(verbose_name=_("Grade"), blank=True, null=True)
    passed = models.BooleanField(verbose_name=_('passed'), default=False)
    date = models.DateTimeField(verbose_name=_('Date'), default=datetime.utcnow(), blank=True, null=True)

    class Meta:
        verbose_name = _("selection")

    def __str__(self):
        return 'Selection:{}'.format(self.project.name)


class PM10(models.Model):
    project = models.ForeignKey('Project')
    value = models.SmallIntegerField(verbose_name=_('Value'))
    date = models.DateTimeField(verbose_name=_('Date'))

    class Meta:
        verbose_name = _('pm10')

    def __str__(self):
        return 'PM10:{}'.format(self.value)


class Notification(models.Model):
    label = models.CharField(verbose_name=_('label'), max_length=256)
    type = models.SmallIntegerField(verbose_name=_('type'))
    project_url = models.CharField(verbose_name=_('project_url'), max_length=128)
    processed = models.BooleanField(verbose_name=_('processed'), default=False)
    date = models.DateTimeField(verbose_name=_('Date'), blank=True, null=True, default=datetime.utcnow())

    class Meta:
        verbose_name = _('notification')

    def __str__(self):
        return 'Notification:{} type:{}'.format(self.label, self.type)


class Picture(models.Model):
    """This is a small demo using just two fields. The slug field is really not
    necessary, but makes the code simpler. ImageField depends on PIL or
    pillow (where Pillow is easily installable in a virtualenv. If you have
    problems installing pillow, use a more generic FileField instead.

    """
    review = models.ForeignKey(ApplicationReview)
    file = models.ImageField(upload_to="pictures")
    slug = models.SlugField(max_length=50, blank=True)

    def __unicode__(self):
        return self.file.name

    @models.permalink
    def get_absolute_url(self):
        return ('upload-new', )

    def save(self, *args, **kwargs):
        #self.slug = self.file.name
        super(Picture, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """delete -- Remove to leave file."""
        self.file.delete(False)
        super(Picture, self).delete(*args, **kwargs)


class ControlItem(models.Model):
    number_request = models.CharField(verbose_name=_('Number and Request'), max_length=128)
    conclusion = models.CharField(verbose_name=_('Conclusion'), max_length=128)

    def __str__(self):
        return 'number_request:{}'.format(self.number_request)


class BaseItem(models.Model):
    number_request = models.CharField(verbose_name=_('Number and Request'), max_length=128)
    count_standard = models.CharField(verbose_name=_('Count Standard'), max_length=128)
    deserved_score = models.FloatField(verbose_name=_('Deserved Score'))
    actual_score = models.FloatField(verbose_name=_('Actual Score'))

    def __str__(self):
        return 'number_request:{}'.format(self.number_request)


class GeneralItem(BaseItem):
    pass


class ExcellentItem(BaseItem):
    pass


class ElementEvaluationForm(models.Model):
    project = models.ForeignKey(Project)
    number = models.CharField(verbose_name=_('Number'), max_length=128, blank=True, null=True)
    date = models.DateField(verbose_name=_('Date'), blank=True, null=True)
    construction_phase = models.CharField(verbose_name=_('construction_phase'), max_length=64, blank=True, null=True)
    evaluation_indicator = models.CharField(verbose_name=_('evaluation_indicator'), max_length=64, blank=True, null=True)
    construction_part = models.CharField(verbose_name=_('construction_part'), max_length=64, blank=True, null=True)

    control_items = models.ManyToManyField(ControlItem)
    general_items = models.ManyToManyField(GeneralItem)
    excellent_items = models.ManyToManyField(ExcellentItem)

    evaluation_result = models.CharField(verbose_name=_('Evaluation Result'), max_length=2048, blank=True, null=True)
    development_unit_sign = models.CharField(verbose_name=_('development_unit_sign'), max_length=256, blank=True, null=True)
    supervision_unit_sign = models.CharField(verbose_name=_('supervision_unit_sign'), max_length=256, blank=True, null=True)
    construction_unit_sign = models.CharField(verbose_name=_('construction_unit_sign'), max_length=256, blank=True, null=True)


    def __str__(self):
        return 'ElementEvaluationForm:{}'.format(self.project.name)


class BatchEvaluationForm(models.Model):
    project = models.ForeignKey(Project)
    number = models.CharField(verbose_name=_('Number'), max_length=128, blank=True, null=True)
    date = models.DateField(verbose_name=_('Date'), blank=True, null=True)
    evaluation_phase = models.CharField(verbose_name=_('evaluation_phase'), max_length=64, blank=True, null=True)

    env_evaluation_score = models.FloatField(verbose_name=_('env_evaluation_score'), blank=True, null=True)
    env_real_score = models.FloatField(verbose_name=_('env_real_score'), blank=True, null=True)
    materials_evaluation_score = models.FloatField(verbose_name=_('materials_evaluation_score'), blank=True, null=True)
    materials_real_score = models.FloatField(verbose_name=_('materials_real_score'), blank=True, null=True)
    water_evaluation_score = models.FloatField(verbose_name=_('water_evaluation_score'), blank=True, null=True)
    water_real_score = models.FloatField(verbose_name=_('water_real_score'), blank=True, null=True)
    power_evaluation_score = models.FloatField(verbose_name=_('power_evaluation_score'), blank=True, null=True)
    power_real_score = models.FloatField(verbose_name=_('power_real_score'), blank=True, null=True)
    land_evaluation_score = models.FloatField(verbose_name=_('land_evaluation_score'), blank=True, null=True)
    land_real_score = models.FloatField(verbose_name=_('land_real_score'), blank=True, null=True)
    total_evaluation_score = models.FloatField(verbose_name=_('total_evaluation_score'), blank=True, null=True)
    total_real_score = models.FloatField(verbose_name=_('total_real_score'), blank=True, null=True)

    evaluation_result = models.CharField(verbose_name=_('Evaluation Result'), max_length=2048, blank=True, null=True)
    #development_unit_sign = models.CharField(verbose_name=_('development_unit_sign'), max_length=256, blank=True, null=True)
    #supervision_unit_sign = models.CharField(verbose_name=_('supervision_unit_sign'), max_length=256, blank=True, null=True)
    #construction_unit_sign = models.CharField(verbose_name=_('construction_unit_sign'), max_length=256, blank=True, null=True)


    def __str__(self):
        return 'BatchEvaluationForm:{}'.format(self.project.name)


class StageEvaluationForm(models.Model):
    project = models.ForeignKey(Project)
    number = models.CharField(verbose_name=_('Number'), max_length=128, blank=True, null=True)
    date = models.DateField(verbose_name=_('Date'), blank=True, null=True)
    evaluation_phase = models.CharField(verbose_name=_('evaluation_phase'), max_length=64, blank=True, null=True)

    evaluation_result = models.CharField(verbose_name=_('Evaluation Result'), max_length=2048, blank=True, null=True)
    #development_unit_sign = models.CharField(verbose_name=_('development_unit_sign'), max_length=256, blank=True, null=True)
    #supervision_unit_sign = models.CharField(verbose_name=_('supervision_unit_sign'), max_length=256, blank=True, null=True)
    #construction_unit_sign = models.CharField(verbose_name=_('construction_unit_sign'), max_length=256, blank=True, null=True)


    def __str__(self):
        return 'StageEvaluationForm:{}'.format(self.project.name)


class UnitEvaluationForm(models.Model):
    project = models.ForeignKey(Project)
    number = models.CharField(verbose_name=_('Number'), max_length=128, blank=True, null=True)
    date = models.DateField(verbose_name=_('Date'), blank=True, null=True)

    foundation_stage_score = models.FloatField(verbose_name=_('foundation_stage_score'), blank=True, null=True)
    foundation_real_score = models.FloatField(verbose_name=_('foundation_real_score'), blank=True, null=True)
    architecture_stage_score = models.FloatField(verbose_name=_('architecture_stage_score'), blank=True, null=True)
    architecture_real_score = models.FloatField(verbose_name=_('architecture_real_score'), blank=True, null=True)
    install_stage_score = models.FloatField(verbose_name=_('install_stage_score'), blank=True, null=True)
    install_real_score = models.FloatField(verbose_name=_('install_real_score'), blank=True, null=True)
    total_evaluation_score = models.FloatField(verbose_name=_('total_evaluation_score'), blank=True, null=True)
    total_real_score = models.FloatField(verbose_name=_('total_real_score'), blank=True, null=True)

    evaluation_result = models.CharField(verbose_name=_('Evaluation Result'), max_length=2048, blank=True, null=True)
    #development_unit_sign = models.CharField(verbose_name=_('development_unit_sign'), max_length=256, blank=True, null=True)
    #supervision_unit_sign = models.CharField(verbose_name=_('supervision_unit_sign'), max_length=256, blank=True, null=True)
    #construction_unit_sign = models.CharField(verbose_name=_('construction_unit_sign'), max_length=256, blank=True, null=True)


    def __str__(self):
        return 'UnitEvaluationForm:{}'.format(self.project.name)






