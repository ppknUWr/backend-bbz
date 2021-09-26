from django.contrib import admin
import json
from .models import models, BibliographyTemplateModel, MetaDBInfo

# Register your models here.


"""
Loop register all models for /admin site. MODELS are list got from models.py
"""

for model in models:
    @admin.register(model)
    class BibliographyTemplateModelAdmin(admin.ModelAdmin):
        list_display = ('book_author', 'title', 'publication_date', 'isbn_or_issn_number', 'doi_number', 'pages')
        list_filter = ('publication_date', 'pages')
        search_fields = ['book_author', 'title', 'publication_date', 'isbn_or_issn_number', 'doi_number']

@admin.register(MetaDBInfo)
class MetaDBInfoAdmin(admin.ModelAdmin):
    list_display = ('db_name', 'real_db_name', 'author')
    list_filter = ('db_name', 'real_db_name', 'author')
    search_fields = ['db_name', 'real_db_name', 'author']

