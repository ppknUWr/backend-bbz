from django.db import models
import copy

# Create your models here.

"""
Important:
    id = models.IntegerField(db_column='ID', primary_key=True)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE) #2
    co_authors = models.CharField(max_length=256) #3
    editor = models.CharField(max_length = 256) #4
    title = models.TextField() #5
    subtitle = models.TextField() #6
    original_edition = models.TextField() #7
    series = models.TextField() #8
    publication_date = models.TextField() #9
    publication = models.TextField() #10
    publication_place = models.TextField() #11
    publisher = models.TextField() #12
    source = models.TextField() #13
    number = models.TextField() #14
    notebook = models.TextField() #15
    pages = models.TextField() #16
    language = models.TextField() #17
    isbn_or_issn_number = models.TextField() #18
    doi_number = models.TextField() #19
    link = models.URLField(max_length=200) #20
    keywords_and_content = models.TextField() #21
    comments = models.TextField() #22
"""