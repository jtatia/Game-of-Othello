# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-04-10 13:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Othello', '0003_auto_20180408_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamedb',
            name='gameOver',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='gamedb',
            name='lastValid',
            field=models.IntegerField(default=1),
        ),
    ]
