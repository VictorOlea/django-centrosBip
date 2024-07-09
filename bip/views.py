from django.shortcuts import render
from .models import centrosBip
from django.http import JsonResponse

# Create your views here.
def centros_bip(r):
    centroBip = centrosBip.objects.all()
    return render(r, 'centros_bip.html', {
        'centrosBip': centroBip
    })

def centros_bip_json(r):
    centroBip = list(centrosBip.objects.values())
    return JsonResponse(centroBip, safe=False)
    