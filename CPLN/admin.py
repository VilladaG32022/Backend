from __future__ import unicode_literals

from django.contrib import admin
from .models import *
from django.apps import apps
from django.utils.html import format_html
    
my_models = apps.get_models()

#modeladmin
class IngredientInline(admin.StackedInline):
    extra = 1
    model = Ingredient

class FamilyVolunteerInline(admin.StackedInline):
    extra = 1
    model = FamilyVolunteer

class InventoryInline(admin.StackedInline):
    extra = 1
    model = Inventory

class ProductDonationInline(admin.StackedInline):
    extra = 1
    model = ProductDonation

class MonetaryDonationInline(admin.StackedInline):
    extra = 1
    model = MonetaryDonation

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "neighborhood", "status")
    ordering = ("last_name",)
    list_filter = ("neighborhood",)
    list_display_links = ("last_name",)
    list_editable = ("status",)
    list_per_page = 10


@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    list_display = ("title", "description")
    list_filter = ("title",)
    list_per_page = 5

@admin.register(Family)
class FamilyAdmin(admin.ModelAdmin):
    inlines =  (FamilyVolunteerInline, InventoryInline)
    list_display = ('name',)

@admin.register(Lunch)
class LunchAdmin(admin.ModelAdmin):
    def action(self, obj):
        if not obj:
            return
        return format_html(f'<a href="/calc-lunch/{obj.id}">Calcular menu</a>')
    inlines =  (IngredientInline, )
    list_display = ('description', 'action')

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    inlines =  (ProductDonationInline, MonetaryDonationInline)
    list_display = ('donator', 'date')

# Register your models here.

for model in my_models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass