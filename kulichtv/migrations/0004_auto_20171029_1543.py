# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-29 15:43
from __future__ import unicode_literals

from django.db import migrations, models
import kulichtv.models


class Migration(migrations.Migration):

    dependencies = [
        ('kulichtv', '0003_game_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='pic',
            field=models.ImageField(default='None/none.thumbnail', upload_to=kulichtv.models.Game.get_pic_url),
        ),
    ]
