from __future__ import unicode_literals
from django import forms
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy, reverse



from django.template import Context
from mongoengine import *



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
    page_all
   )

MONGO_DATABASE_NAME = 'wikipedia_candidates'
DEFAULT_CONNECTION_NAME = connect(MONGO_DATABASE_NAME)


# class PollsListView(ListView):
#     template_name = 'polls/search.html'
    

#     def get_queryset(self, *args, **kwargs):
#         qs = page_all.objects.all()
#         return qs 




class CandidateListView(ListView):

    template_name = 'politicians/search_result.html'

    def get_queryset(self, *args, **kwargs):
        qs = page_all.objects.all()
        query = self.request.GET.get("q", None)
        if query is not None:
            query = query.strip()
            qs = qs.filter(
                Q(candiate_name__icontains=query) |
                Q(content_wiki__icontains=query) |
                Q(reference_wiki__icontains=query)|
                Q(title_wiki__icontains=query)
            )

        return qs 

    def get_context_data(self, *args, **kwargs):
        context = super(CandidateListView, self).get_context_data(*args, **kwargs)
        return context


class CandidateDetailView(DetailView):
    queryset = page_all.objects.all()

    def get_objects(self):
        return page_all.objects.get(id =_id)