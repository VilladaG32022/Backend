from __future__ import unicode_literals

from django.contrib import admin
from .models import *
from django.apps import apps
    
my_models = apps.get_models()

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name","dateOfBirth", "neighborhood","telephone","email","is_candidate")
    ordering = ("last_name",)
    search_fields = ("neighborhood","last_name")
    list_filter = ("neighborhood",)
    list_editable = ("is_candidate",)
    list_display_links = ("last_name",)
    list_per_page = 8

# Register your models here.

for model in my_models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass