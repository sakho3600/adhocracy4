# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-07 08:41
from __future__ import unicode_literals

import adhocracy4.images.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('a4projects', '0009_optional_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image_copyright',
            field=adhocracy4.images.fields.ImageCopyrightField(blank=True, help_text='Copyright shown in the header image', max_length=120, verbose_name='Header image copyright'),
        ),
        migrations.AddField(
            model_name='project',
            name='tile_image_copyright',
            field=adhocracy4.images.fields.ImageCopyrightField(blank=True, help_text='Copyright shown in the tile image', max_length=120, verbose_name='Tile image copyright'),
        ),
    ]