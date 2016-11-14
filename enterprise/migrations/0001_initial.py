# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationReview',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grade', models.CharField(max_length=64, verbose_name='Grade', choices=[('green_building', 'green_building'), ('green_building_demo', 'green_building_demo')])),
                ('date', models.DateTimeField(default=datetime.datetime(2016, 11, 2, 7, 53, 56, 118000), verbose_name='Date')),
                ('achievement', models.FileField(upload_to=b'video', null=True, verbose_name='Achievement', blank=True)),
                ('contact', models.CharField(max_length=32, null=True, verbose_name='contact', blank=True)),
                ('phone', models.CharField(max_length=32, null=True, verbose_name='phone', blank=True)),
                ('content', models.CharField(max_length=2048, null=True, verbose_name='content', blank=True)),
                ('company_opinion', models.CharField(max_length=2048, null=True, verbose_name='company_opinion', blank=True)),
                ('management_opinion', models.CharField(max_length=2048, null=True, verbose_name='management_opinion', blank=True)),
                ('approved', models.BooleanField(default=False, verbose_name='approved')),
                ('general', models.CharField(max_length=2048, null=True, verbose_name='Project General', blank=True)),
                ('characteristic', models.CharField(max_length=2048, null=True, verbose_name='Project Characteristic', blank=True)),
                ('construct_management', models.CharField(max_length=2048, null=True, verbose_name='Construct Management', blank=True)),
                ('env_protection_measure', models.CharField(max_length=2048, null=True, verbose_name='Environment Protection Measure', blank=True)),
                ('economize_materials', models.CharField(max_length=2048, null=True, verbose_name='Economize on raw materials', blank=True)),
                ('economize_waters', models.CharField(max_length=2048, null=True, verbose_name='Economize on water', blank=True)),
                ('economize_powers', models.CharField(max_length=2048, null=True, verbose_name='Economize on power', blank=True)),
                ('economize_land', models.CharField(max_length=2048, null=True, verbose_name='Economize on land', blank=True)),
                ('new_technology', models.CharField(max_length=2048, null=True, verbose_name='New Technology', blank=True)),
                ('new_equipment', models.CharField(max_length=2048, null=True, verbose_name='New Equipment', blank=True)),
                ('new_craft', models.CharField(max_length=2048, null=True, verbose_name='New Materials and  Craft', blank=True)),
                ('industrialization', models.CharField(max_length=2048, null=True, verbose_name='Industrialization of construction industry', blank=True)),
                ('comprehensive_benefit', models.CharField(max_length=2048, null=True, verbose_name='Comprehensive Benefit', blank=True)),
            ],
            options={
                'ordering': ['date'],
                'verbose_name': 'application_review',
                'permissions': (('approve_review', 'Can approve reviews'), ('deny_review', 'Can deny reviews'), ('submit_review', 'Can submit reviews'), ('print_review', 'Can print reviews')),
            },
        ),
        migrations.CreateModel(
            name='BaseItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number_request', models.CharField(max_length=128, verbose_name='Number and Request')),
                ('count_standard', models.CharField(max_length=128, verbose_name='Count Standard')),
                ('deserved_score', models.FloatField(verbose_name='Deserved Score')),
                ('actual_score', models.FloatField(verbose_name='Actual Score')),
            ],
        ),
        migrations.CreateModel(
            name='BatchEvaluationForm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(max_length=128, null=True, verbose_name='Number', blank=True)),
                ('date', models.DateField(null=True, verbose_name='Date', blank=True)),
                ('evaluation_phase', models.CharField(max_length=64, null=True, verbose_name='evaluation_phase', blank=True)),
                ('env_evaluation_score', models.FloatField(null=True, verbose_name='env_evaluation_score', blank=True)),
                ('env_real_score', models.FloatField(null=True, verbose_name='env_real_score', blank=True)),
                ('materials_evaluation_score', models.FloatField(null=True, verbose_name='materials_evaluation_score', blank=True)),
                ('materials_real_score', models.FloatField(null=True, verbose_name='materials_real_score', blank=True)),
                ('water_evaluation_score', models.FloatField(null=True, verbose_name='water_evaluation_score', blank=True)),
                ('water_real_score', models.FloatField(null=True, verbose_name='water_real_score', blank=True)),
                ('power_evaluation_score', models.FloatField(null=True, verbose_name='power_evaluation_score', blank=True)),
                ('power_real_score', models.FloatField(null=True, verbose_name='power_real_score', blank=True)),
                ('land_evaluation_score', models.FloatField(null=True, verbose_name='land_evaluation_score', blank=True)),
                ('land_real_score', models.FloatField(null=True, verbose_name='land_real_score', blank=True)),
                ('total_evaluation_score', models.FloatField(null=True, verbose_name='total_evaluation_score', blank=True)),
                ('total_real_score', models.FloatField(null=True, verbose_name='total_real_score', blank=True)),
                ('evaluation_result', models.CharField(max_length=2048, null=True, verbose_name='Evaluation Result', blank=True)),
            ],
            options={
                'verbose_name': 'Batch Evaluation Form',
            },
        ),
        migrations.CreateModel(
            name='ControlItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number_request', models.CharField(max_length=128, verbose_name='Number and Request')),
                ('conclusion', models.CharField(max_length=128, verbose_name='Conclusion')),
            ],
            options={
                'verbose_name': 'Control Items',
            },
        ),
        migrations.CreateModel(
            name='ElementEvaluationForm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(max_length=128, null=True, verbose_name='Number', blank=True)),
                ('date', models.DateField(null=True, verbose_name='Date', blank=True)),
                ('construction_phase', models.CharField(max_length=64, null=True, verbose_name='construction_phase', blank=True)),
                ('evaluation_indicator', models.CharField(max_length=64, null=True, verbose_name='evaluation_indicator', blank=True)),
                ('construction_part', models.CharField(max_length=64, null=True, verbose_name='construction_part', blank=True)),
                ('evaluation_result', models.CharField(max_length=2048, null=True, verbose_name='Evaluation Result', blank=True)),
                ('development_unit_sign', models.CharField(max_length=256, null=True, verbose_name='development_unit_sign', blank=True)),
                ('supervision_unit_sign', models.CharField(max_length=256, null=True, verbose_name='supervision_unit_sign', blank=True)),
                ('construction_unit_sign', models.CharField(max_length=256, null=True, verbose_name='construction_unit_sign', blank=True)),
                ('control_items', models.ManyToManyField(to='enterprise.ControlItem', verbose_name='Control Items')),
            ],
            options={
                'verbose_name': 'Element Evaluation Form',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=256, verbose_name='label')),
                ('type', models.SmallIntegerField(verbose_name='type', choices=[(1, 'Submission'), (2, 'Application Review')])),
                ('project_url', models.CharField(max_length=128, verbose_name='project_url')),
                ('processed', models.BooleanField(default=False, verbose_name='processed')),
                ('date', models.DateTimeField(default=datetime.datetime(2016, 11, 2, 7, 53, 56, 124000), null=True, verbose_name='Date', blank=True)),
            ],
            options={
                'verbose_name': 'Notification',
            },
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.ImageField(upload_to=b'pictures')),
                ('slug', models.SlugField(blank=True)),
                ('review', models.ForeignKey(to='enterprise.ApplicationReview')),
            ],
        ),
        migrations.CreateModel(
            name='PM10',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.SmallIntegerField(verbose_name='Value')),
                ('date', models.DateTimeField(verbose_name='Date')),
            ],
            options={
                'verbose_name': 'pm10',
            },
        ),
        migrations.CreateModel(
            name='ProgressMonitor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(verbose_name='Date')),
                ('pm10_threshold', models.IntegerField(verbose_name='pm10_threshold')),
            ],
            options={
                'verbose_name': 'progress_monitor',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('PrjNum', models.CharField(default=b'3202041503050102', max_length=256, verbose_name='prj_num')),
                ('name', models.CharField(max_length=256, verbose_name='project_name')),
                ('location', models.CharField(max_length=256, null=True, verbose_name='location', blank=True)),
                ('area', models.FloatField(null=True, verbose_name='area', blank=True)),
                ('cost', models.FloatField(null=True, verbose_name='cost', blank=True)),
                ('structure_type', models.CharField(max_length=32, null=True, verbose_name='structure_type', blank=True)),
                ('start_date', models.DateField(null=True, verbose_name='start_date', blank=True)),
                ('end_date', models.DateField(null=True, verbose_name='end_date', blank=True)),
                ('description', models.CharField(max_length=1024, null=True, verbose_name='description', blank=True)),
                ('construct_company', models.CharField(max_length=256, null=True, verbose_name='construct_company', blank=True)),
                ('owner', models.CharField(max_length=256, null=True, verbose_name='owner', blank=True)),
                ('postal_address', models.CharField(max_length=256, null=True, verbose_name='postal_address', blank=True)),
                ('zipcode', models.CharField(max_length=6, null=True, verbose_name='zipcode', blank=True)),
                ('finish_vote_date', models.DateTimeField(null=True, verbose_name='Finish Vote Date', blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'project',
            },
        ),
        migrations.CreateModel(
            name='Selection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grade', models.SmallIntegerField(null=True, verbose_name='Grade', blank=True)),
                ('passed', models.BooleanField(default=False, verbose_name='passed')),
                ('date', models.DateTimeField(null=True, verbose_name='Date', blank=True)),
                ('project', models.ForeignKey(to='enterprise.Project')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'selection',
                'permissions': (('thumb_up', 'Can thumb up projects'), ('thumb_down', 'Can thumb down projects')),
            },
        ),
        migrations.CreateModel(
            name='SelfEvaluation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('completion_date', models.DateTimeField(verbose_name='completion_date')),
                ('awards', models.CharField(max_length=256, null=True, verbose_name='awards', blank=True)),
                ('project', models.ForeignKey(to='enterprise.Project')),
            ],
            options={
                'verbose_name': 'self_evaluation',
            },
        ),
        migrations.CreateModel(
            name='StageEvaluationForm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(max_length=128, null=True, verbose_name='Number', blank=True)),
                ('date', models.DateField(null=True, verbose_name='Date', blank=True)),
                ('evaluation_phase', models.CharField(max_length=64, null=True, verbose_name='evaluation_phase', blank=True)),
                ('evaluation_result', models.CharField(max_length=2048, null=True, verbose_name='Evaluation Result', blank=True)),
                ('project', models.ForeignKey(verbose_name='project', to='enterprise.Project')),
            ],
            options={
                'verbose_name': 'Stage Evaluation Form',
            },
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grade', models.CharField(max_length=64, verbose_name='Grade', choices=[('green_building', 'green_building'), ('green_building_demo', 'green_building_demo')])),
                ('date', models.DateTimeField(default=datetime.datetime(2016, 11, 2, 7, 53, 56, 117000), verbose_name='Date')),
                ('person_in_charge', models.CharField(max_length=32, null=True, verbose_name='person_in_charge', blank=True)),
                ('phone1', models.CharField(max_length=32, null=True, verbose_name='phone1', blank=True)),
                ('technical_in_charge', models.CharField(max_length=32, null=True, verbose_name='technical_in_charge', blank=True)),
                ('phone2', models.CharField(max_length=32, null=True, verbose_name='phone2', blank=True)),
                ('company_technical_in_charge', models.CharField(max_length=32, null=True, verbose_name='company_technical_in_charge', blank=True)),
                ('phone3', models.CharField(max_length=32, null=True, verbose_name='phone3', blank=True)),
                ('content', models.CharField(max_length=2048, null=True, verbose_name='content', blank=True)),
                ('measures', models.CharField(max_length=1024, null=True, verbose_name='measures', blank=True)),
                ('schedule', models.CharField(max_length=1024, null=True, verbose_name='schedule', blank=True)),
                ('benefits', models.CharField(max_length=1024, null=True, verbose_name='benefits', blank=True)),
                ('company_opinion', models.CharField(max_length=2048, null=True, verbose_name='company_opinion', blank=True)),
                ('management_opinion', models.CharField(max_length=2048, null=True, verbose_name='management_opinion', blank=True)),
                ('approved', models.BooleanField(default=False, verbose_name='approved')),
                ('project', models.ForeignKey(to='enterprise.Project')),
            ],
            options={
                'ordering': ['date'],
                'verbose_name': 'submission',
                'permissions': (('approve_submission', 'Can approve submissions'), ('deny_submission', 'Can deny submissions'), ('submit_submission', 'Can submit submissions'), ('print_submission', 'Can print submissions')),
            },
        ),
        migrations.CreateModel(
            name='UnitEvaluationForm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(max_length=128, null=True, verbose_name='Number', blank=True)),
                ('date', models.DateField(null=True, verbose_name='Date', blank=True)),
                ('foundation_stage_score', models.FloatField(null=True, verbose_name='foundation_stage_score', blank=True)),
                ('foundation_real_score', models.FloatField(null=True, verbose_name='foundation_real_score', blank=True)),
                ('architecture_stage_score', models.FloatField(null=True, verbose_name='architecture_stage_score', blank=True)),
                ('architecture_real_score', models.FloatField(null=True, verbose_name='architecture_real_score', blank=True)),
                ('install_stage_score', models.FloatField(null=True, verbose_name='install_stage_score', blank=True)),
                ('install_real_score', models.FloatField(null=True, verbose_name='install_real_score', blank=True)),
                ('total_evaluation_score', models.FloatField(null=True, verbose_name='total_evaluation_score', blank=True)),
                ('total_real_score', models.FloatField(null=True, verbose_name='total_real_score', blank=True)),
                ('evaluation_result', models.CharField(max_length=2048, null=True, verbose_name='Evaluation Result', blank=True)),
                ('project', models.ForeignKey(verbose_name='project', to='enterprise.Project')),
            ],
            options={
                'verbose_name': 'Unit Evaluation Form',
            },
        ),
        migrations.CreateModel(
            name='ExcellentItem',
            fields=[
                ('baseitem_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='enterprise.BaseItem')),
            ],
            options={
                'verbose_name': 'Excellent Items',
            },
            bases=('enterprise.baseitem',),
        ),
        migrations.CreateModel(
            name='GeneralItem',
            fields=[
                ('baseitem_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='enterprise.BaseItem')),
            ],
            options={
                'verbose_name': 'General Items',
            },
            bases=('enterprise.baseitem',),
        ),
        migrations.AddField(
            model_name='progressmonitor',
            name='project',
            field=models.ForeignKey(to='enterprise.Project'),
        ),
        migrations.AddField(
            model_name='pm10',
            name='project',
            field=models.ForeignKey(to='enterprise.Project'),
        ),
        migrations.AddField(
            model_name='elementevaluationform',
            name='project',
            field=models.ForeignKey(verbose_name='project', to='enterprise.Project'),
        ),
        migrations.AddField(
            model_name='batchevaluationform',
            name='project',
            field=models.ForeignKey(verbose_name='project', to='enterprise.Project'),
        ),
        migrations.AddField(
            model_name='applicationreview',
            name='project',
            field=models.ForeignKey(to='enterprise.Project'),
        ),
        migrations.AddField(
            model_name='elementevaluationform',
            name='excellent_items',
            field=models.ManyToManyField(to='enterprise.ExcellentItem', verbose_name='Excellent Items'),
        ),
        migrations.AddField(
            model_name='elementevaluationform',
            name='general_items',
            field=models.ManyToManyField(to='enterprise.GeneralItem', verbose_name='General Items'),
        ),
    ]
