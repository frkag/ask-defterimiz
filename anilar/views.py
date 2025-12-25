from django.shortcuts import render
from .models import Ani

def anasayfa(request):
    # Tüm anıları veritabanından çekiyoruz
    tum_anilar = Ani.objects.all().order_by('-tarih') 
    return render(request, 'askimiz.html', {'anilar': tum_anilar})