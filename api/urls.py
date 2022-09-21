from django.urls import path
from api import views
#from .views import RegisterAPI


urlpatterns = [
    path('UserPage/', views.getUserPage),
    path('Inscriptions/', views.inscriptions),
    path('Notices/', views.notices),
]
