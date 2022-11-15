from django.shortcuts import render
from django.views.generic.base import TemplateView

from CPLN.models import Lunch
# Create your views here.
class CalcLunch(TemplateView):
    template_name = "admin/lanch_calc.html"

    def get_context_data(self, **kwargs):
        lunch = Lunch.objects.get(pk=kwargs.get('pk'))
        return {'lunch':lunch, 'qty': self.request.GET.get('qty',1) }