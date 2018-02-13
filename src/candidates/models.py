from __future__ import unicode_literals
from django.db import models
import django.db.models.options as options
from django.conf import settings
from django.urls import reverse
from django.db import models
from django.db.models import F
from django.core.exceptions import ValidationError
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User



from mongoengine import Document, EmbeddedDocument, fields
from mongoengine import *
MONGO_DATABASE_NAME = 'wikipedia_candidates'

DEFAULT_CONNECTION_NAME = connect(MONGO_DATABASE_NAME)

# options.DEFAULT_NAMES = options.DEFAULT_NAMES + ('in_db',)


class PageAllCandidates(Document):
        _id = fields.StringField()
        candiate_name= fields.StringField()
        content_wiki= fields.StringField()
        reference_wiki= fields.StringField()
        title_wiki= fields.StringField()
        url_wiki= fields.StringField()
        candidate_slug = fields.StringField()

        # def __str__(self):
        #     return self.candidate_slug

        # def save(self, *args, **kwargs):
        #           self.candidate_slug = slugify(self.candidate_slug)
        #           super(PageAllCandidates, self).save(*args, **kwargs)     

        # def get_absolute_url(self):
        #     return reverse("candidates:candidatedetail", kwargs={"slug":self.candidate_slug})    



class page_rec(Document):
        _id = fields.StringField()
        candiate_name= fields.StringField()
        content_wiki= fields.StringField()
        reference_wiki= fields.StringField()
        title_wiki= fields.StringField()
        url_wiki= fields.StringField()
        candidate_slug = fields.StringField()


        def get_absolute_url(self):
            return reverse("candidates:candidatedetail", kwargs={"slug":self.candidate_slug})    


class page_all(Document):
        _id = fields.StringField()
        candiate_name= fields.StringField()
        content_wiki= fields.StringField()
        reference_wiki= fields.StringField()
        title_wiki= fields.StringField()
        url_wiki= fields.StringField()

#         candid =str(candiate_name)
#         candidate_slug = candid.replace(' ', '')

        # def get_absolute_url(self):
        #     return reverse("candidates:candidatedetail", kwargs={"slug":self.candidate_slug})   