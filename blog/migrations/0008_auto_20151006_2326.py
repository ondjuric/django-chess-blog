# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20151006_2054'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image_url',
            new_name='img_name',
        ),
    ]
