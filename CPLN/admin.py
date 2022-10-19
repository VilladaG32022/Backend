from __future__ import unicode_literals

from django.contrib import admin
from .models import *
from django.apps import apps
from api.serializers import VolunteerSerializer
    
my_models = apps.get_models()


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "neighborhood")
    ordering = ("last_name",)
    list_filter = ("neighborhood",)
    list_display_links = ("last_name",)
    #list_editable = ("status",)
    list_per_page = 10
    actions = ["add_volunteer"]

    def add_volunteer(modeladmin, request, queryset):
        for candidate in queryset:
            serializeobj = VolunteerSerializer(data=candidate)
            if serializeobj.is_valid():
                VolunteerSerializer(candidate).save()
                candidate.delete()

#modeladmin


@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    list_display = ("title", "description")
    list_filter = ("title",)
    list_per_page = 5

# Register your models here.

for model in my_models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass