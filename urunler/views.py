from django.shortcuts import render,get_object_or_404
from .models import Urunler,Kategoriler

# Create your views here.



def index(request):
    urunler = Urunler.objects.filter(anasayfa=True)
    return render(request, 'index.html',{"products":urunler})

def urundetaysayfa(request, slug):
    urun = get_object_or_404(Urunler,slug=slug)
    return render(request, 'urun.html',{"urun":urun}) 


def kategoridetay(request,slug):
    kategori = get_object_or_404(Kategoriler,slug=slug)
    urunler = Urunler.objects.filter(kategori=kategori)
    return render(request, 'kategoridetay.html',{"kategori":kategori,"products":urunler})

