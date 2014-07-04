# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id')),
                ('name', models.CharField(max_length=256, verbose_name='project_name')),
                ('location', models.CharField(max_length=256, verbose_name='location', blank=True)),
                ('description', models.CharField(max_length=1024, verbose_name='description', blank=True)),
                ('construct_company', models.CharField(max_length=256, verbose_name='construct_company', blank=True)),
                ('contact', models.CharField(max_length=128, verbose_name='contact', blank=True)),
                ('phone', models.CharField(max_length=30, verbose_name='phone', blank=True)),
                ('address', models.CharField(max_length=256, verbose_name='address', blank=True)),
                ('zipcode', models.CharField(max_length=6, verbose_name='zipcode', blank=True)),
            ],
            options={
                'ordering': [b'name'],
                'verbose_name': 'project',
            },
            bases=(models.Model,),
        ),
    ]
