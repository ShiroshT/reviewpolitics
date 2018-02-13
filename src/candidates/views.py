from __future__ import unicode_literals
from django import forms
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from mongogeneric.detail import (SingleDocumentMixin, DetailView, 
                                 SingleDocumentTemplateResponseMixin, BaseDetailView)


from django.template import Context
from mongoengine import *

from django.views.generic import (
    # DeleteView,
    # DetailView, 
    ListView
    # CreateView, 
    # FormView,
    # UpdateView
)

# Model Import 
# from .forms import PoliticianModelForm
from .models import (
    PageAllCandidates,
    page_all,
    page_rec

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

        qs = page_rec.objects.all()
 
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


# class CandidateDetailView(DetailView):
#     queryset = page_rec.objects.all()
#     print 'queryset', queryset
 

    # def get_objects(self):
    #     return page_rec.objects.get(slug_field =page_rec.candidate_slug)


    # def get_slug_field(self): 
    #     return self.slug_field


    # def get_object(self, queryset=None):
    #     """
    #     Returns the object the view is displaying.
    #     By default this requires `self.queryset` and a `pk` or `slug` argument
    #     in the URLconf, but subclasses can override this to return any object.
    #     """
    #     # Use a custom queryset if provided; this is required for subclasses
    #     # like DateDetailView
    #     if queryset is None:
    #         queryset = self.get_queryset()
    #     # Next, try looking up by primary key.
    #     pk = self.kwargs.get(self.pk_url_kwarg)
    #     slug = self.kwargs.get(self.slug_url_kwarg)
    #     if pk is not None:
    #         queryset = queryset.filter(pk=pk)
    #     # Next, try looking up by slug.
    #     if slug is not None and (pk is None or self.query_pk_and_slug):
    #         slug_field = self.get_slug_field()
    #         queryset = queryset.filter(**{slug_field: slug})
    #     # If none of those are defined, it's an error.
    #     if pk is None and slug is None:
    #         raise AttributeError("Generic detail view %s must be called with "
    #                              "either an object pk or a slug."
    #                              % self.__class__.__name__)
    #     try:
    #         # Get the single item from the filtered queryset
    #         obj = queryset.get()
    #     except queryset.model.DoesNotExist:
    #         raise Http404(_("No %(verbose_name)s found matching the query") %
    #                       {'verbose_name': queryset.model._meta.verbose_name})
    #     return obj

class EmbeddedDetailView(BaseEmbeddedFormMixin, DetailView):
    """
    Renders the detail view of a document and and adds a
    form for an embedded object into the template.
    
    See BaseEmbeddedFormMixin for details on the form.
    """
    def get_context_data(self, **kwargs):
        # manually call parents get_context_data without super
        # currently django messes up the super mro chain
        # and for multiple inheritance only one tree is followed
        context = BaseEmbeddedFormMixin.get_context_data(self, **kwargs)
        context.update(DetailView.get_context_data(self, **kwargs))
        return context