# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise', '0002_project_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='zipcode',
            field=models.CharField(max_length=6, null=True, verbose_name='zipcode'),
            preserve_default=True,
        ),
    ]
