from __future__ import unicode_literals

from django.contrib import admin
from .models import *
from django.apps import apps
from api.serializers import CandidateSerializer
from rest_framework.response import Response
from rest_framework import status
    
my_models = apps.get_models()

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "neighborhood", "status")
    ordering = ("last_name",)
    list_filter = ("neighborhood",)
    list_display_links = ("last_name",)
    list_editable = ("status",)
    list_per_page = 10

    actions = ['add_volunteer']

#modeladmin
    def add_volunteer(self, request, queryset):
        for candidate in queryset:
            serializeobj = CandidateSerializer(data=request.queryset, many=True)
            if serializeobj.is_valid():
                serializeobj.save()
                candidate.delete()
                content = {'Candidate created OK': 'Candidate created'}
                return Response(content, status=status.HTTP_200_OK)
            else:
                content = {'BAD_REQUEST': 'Invalid Candidate'}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)
        pass

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