# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256, verbose_name='project_name')),
                ('location', models.CharField(max_length=256, null=True, verbose_name='location')),
                ('description', models.CharField(max_length=1024, null=True, verbose_name='description')),
                ('construct_company', models.CharField(max_length=256, null=True, verbose_name='construct_company')),
                ('contact', models.CharField(max_length=128, null=True, verbose_name='contact')),
                ('phone', models.CharField(max_length=30, null=True, verbose_name='phone')),
            ],
            options={
                'ordering': [b'name'],
                'verbose_name': 'project',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ApplicationReview',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('project', models.ForeignKey(to='enterprise.Project', to_field='id')),
                ('grade', models.SmallIntegerField(verbose_name='grade')),
                ('date', models.DateTimeField(verbose_name='date')),
            ],
            options={
                'ordering': [b'date'],
                'verbose_name': 'application_review',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grade', models.SmallIntegerField(verbose_name='grade')),
                ('project', models.ForeignKey(to='enterprise.Project', to_field='id')),
                ('date', models.DateTimeField(verbose_name='date')),
            ],
            options={
                'ordering': [b'date'],
                'verbose_name': 'submission',
            },
            bases=(models.Model,),
        ),
    ]
