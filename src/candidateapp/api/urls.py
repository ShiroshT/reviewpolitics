from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    CandidatesWikiListAPIView
)

urlpatterns = [
      url(r'^$', CandidatesWikiListAPIView.as_view(), name='candidatelist'), 
]
