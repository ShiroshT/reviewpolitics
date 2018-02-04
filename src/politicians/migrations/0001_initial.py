# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-28 22:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Politician',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortname', models.CharField(max_length=60)),
                ('fullname_polit', models.CharField(max_length=60)),
                ('dateofbirth_polit', models.DateField()),
                ('summary_header', models.TextField(max_length=500)),
                ('detailed_descrpt', models.TextField(max_length=500)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]