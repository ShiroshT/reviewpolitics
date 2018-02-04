# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .forms import PoliticianModelForm
from .models import Politician



class PoliticianModelAdmin(admin.ModelAdmin):
         form = PoliticianModelForm
    # class Meta:
    #     model = Candidate
   



admin.site.register(Politician, PoliticianModelAdmin)