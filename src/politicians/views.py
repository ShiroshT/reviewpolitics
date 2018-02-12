from __future__ import unicode_literals
from django import forms
from django.db.models import Q
from django.shortcuts import render
# from django.urls import reverse_lazy, reverse

from django.views.generic import (
    DeleteView,
    DetailView, 
    ListView, 
    CreateView, 
    FormView,
    UpdateView
)

# Model Import 
# from .forms import PoliticianModelForm
from .models import (
    Politician
   )

# class PolitDetailView(DetailView):


class PolitListView(ListView):

    template_name = 'politicians/search_result.html'

    def get_queryset(self, *args, **kwargs):
        qs = Politician.objects.all()
        query = self.request.GET.get("q", None)
        if query is not None:
            query = query.strip()
            qs = qs.filter(
                Q(shortname__icontains=query) |
                Q(fullname_polit__icontains=query) |
                Q(summary_header__icontains=query)|
                Q(detailed_descrpt__icontains=query)
            )


        return qs 

    def get_context_data(self, *args, **kwargs):
        context = super(PolitListView, self).get_context_data(*args, **kwargs)
        return context


class PolitDetailView(DetailView):
    queryset = Politician.objects.all()

    def get_objects(self):
        return Politician.objects.get(id =id)