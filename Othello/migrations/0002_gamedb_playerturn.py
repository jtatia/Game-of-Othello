# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-04-08 06:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Othello', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamedb',
            name='playerTurn',
            field=models.IntegerField(default=2),
        ),
    ]
