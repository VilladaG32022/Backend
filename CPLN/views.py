from django.shortcuts import render
from django.views.generic.base import TemplateView

from CPLN.models import Lunch, Family
# Create your views here.
class CalcLunch(TemplateView):
    template_name = "admin/lanch_calc.html"

    def get_context_data(self, **kwargs):
        lunch = Lunch.objects.get(pk=kwargs.get('pk'))
        families = Family.objects.all()
        return {'lunch':lunch, 'families':families, 'quantity':self.request.GET.get('qty',0), 'family':self.request.GET.get('family','none')}