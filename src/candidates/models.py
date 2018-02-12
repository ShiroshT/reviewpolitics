from __future__ import unicode_literals
from django.db import models
import django.db.models.options as options

from mongoengine import Document, EmbeddedDocument, fields
from mongoengine import *
MONGO_DATABASE_NAME = 'wikipedia_candidates'

DEFAULT_CONNECTION_NAME = connect(MONGO_DATABASE_NAME)

# options.DEFAULT_NAMES = options.DEFAULT_NAMES + ('in_db',)


class page_all(Document):
        _id = fields.StringField()
        candiate_name= fields.StringField()
        content_wiki= fields.StringField()
        reference_wiki= fields.StringField()
        title_wiki= fields.StringField()
        url_wiki= fields.StringField()