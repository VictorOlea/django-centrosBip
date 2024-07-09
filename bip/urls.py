from django.urls import path
from .views import centros_bip, centros_bip_json

urlpatterns = [
    path('', centros_bip),
    path('bipjson/', centros_bip_json),
]
