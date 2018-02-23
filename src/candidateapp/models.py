# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.urls import reverse
from django.db import models
from django.db.models import F
from django.core.exceptions import ValidationError
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User




class Candidate(models.Model): 
	shortname = models.CharField(max_length=60, unique=True)
	fullname_polit = models.CharField(max_length=60, unique=False)
	politcal_position_current=models.CharField(max_length=150, unique=False)
	dateofbirth_polit = models.DateField()
	summary_header = models.TextField(max_length=500)
	detailed_descrpt = models.TextField(max_length=500)
	timestamp = models.DateTimeField(auto_now_add = True)
	slug = models.SlugField(max_length=15)

	def __str__(self):
		return self.shortname

	def save(self, *args, **kwargs):
              self.slug = slugify(self.shortname)
	      super(Politician, self).save(*args, **kwargs)		

	def get_absolute_url(self):
		return reverse("politicians:politdetail", kwargs={"slug":self.slug})




class CandidatesWiki(models.Model):
    candidate_id = models.AutoField(primary_key=True)
    candiate_name = models.CharField(max_length=255)
    url_wiki = models.CharField(max_length=255, blank=True, null=True)
    title_wiki = models.CharField(max_length=255, blank=True, null=True)
    content_wiki = models.TextField(blank=True, null=True)
    images_wiki = models.TextField(blank=True, null=True)
    references_wiki = models.TextField(blank=True, null=True)
    links_wiki = models.TextField(blank=True, null=True)
    sections_wiki = models.TextField(blank=True, null=True)
    summary_wiki = models.TextField(blank=True, null=True)
    fecha_ini_det = models.DateTimeField(blank=True, null=False)
    fecha_ini_f = models.DateField(blank=True, null=False)
    slug = models.TextField(max_length=15)

    class Meta:
        managed = False
        db_table = 'candidates_wiki'
        get_latest_by = 'fecha_ini_det'


    # def save(self, *args, **kwargs):
    #           self.slug = slugify(self.candiate_name)
    #           super(CandidatesWiki, self).save(*args, **kwargs)   

    def get_absolute_url(self):
        return reverse("candidatesapp:candidatedetail", kwargs={"slug":self.slug})

	