from django.urls import path
from api import views


urlpatterns = [
    path('Inscriptions/', views.inscriptions),
    path('Neighborhoods/', views.Neighborhoods),
    path('Notices/', views.notices),
    path('Notices/Get/', views.MyNotices),
    #path('ListFood/Get/', views.MyList),
]
