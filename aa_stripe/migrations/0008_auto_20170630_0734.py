# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 11:34
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('aa_stripe', '0007_auto_20170630_0557'),
    ]

    operations = [
        migrations.AddField(
            model_name='stripecharge',
            name='content_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='stripecharge',
            name='object_id',
            field=models.PositiveIntegerField(db_index=True, null=True),
        ),
    ]
