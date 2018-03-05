# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-05 19:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('candidateapp', '0003_auto_20180215_2122'),
    ]

    operations = [
        migrations.CreateModel(
            name='CandidateScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('up_votes', models.IntegerField()),
                ('down_votes', models.IntegerField()),
                ('id_candidate_score', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='score', to='candidateapp.CandidatesWiki')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='score', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=500, unique=True)),
                ('review', models.CharField(max_length=500, unique=True)),
                ('date_of_review', models.DateTimeField(auto_now_add=True)),
                ('id_candidate_reivew', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='candidateapp.CandidatesWiki')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]