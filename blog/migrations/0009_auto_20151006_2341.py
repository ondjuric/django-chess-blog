# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20151006_2326'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='img_name',
            new_name='image_name',
        ),
    ]
