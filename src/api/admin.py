from django.contrib import admin
import json
from .models import models

# Register your models here.


"""
Loop register all models for /admin site. MODELS are list got from models.py
"""
for model in models:
    admin.site.register(model)