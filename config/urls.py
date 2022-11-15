from django.urls import include, path
from django.contrib import admin
from api import *

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

from CPLN.views import CalcLunch

urlpatterns = [
    path('', include('api.urls')),
    path("i18n/", include("django.conf.urls.i18n")),
    path('calc-lunch/<int:pk>/', CalcLunch.as_view(), name='calc-lunch'),
    path('calc-lunch/<int:pk>/<int:qty>', CalcLunch.as_view(), name='calc-lunch'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
)
