from __future__ import unicode_literals

from django.contrib import admin
from .models import *
from django.apps import apps
from api.serializers import VolunteerSerializer
    
my_models = apps.get_models()


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "neighborhood", "status")
    ordering = ("last_name",)
    list_filter = ("neighborhood",)
    list_display_links = ("last_name",)
    list_editable = ("status",)
    list_per_page = 10


#modeladmin


@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    list_display = ("title", "description")
    list_filter = ("title",)
    list_per_page = 5

# Register your models here.

class IngredientInline(admin.StackedInline):
    extra = 1
    model = Ingredient
from django.utils.html import format_html
@admin.register(Lunch)
class LunchAdmin(admin.ModelAdmin):
    def action(self, obj):
        if not obj:
            return
        return format_html(f'<button type="button" onclick="/calc-lunch/{obj.id}">Calcular menu</button>')
    inlines =  (IngredientInline, )
    list_display = ('description', 'action')



for model in my_models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass