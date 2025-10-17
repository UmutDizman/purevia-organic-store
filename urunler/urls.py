
from django.urls import path
from . import views

app_name = 'purevia'



urlpatterns = [
    path("", views.index, name="index"),
    path('kategori/<slug:slug>/', views.kategoridetay, name='kategoridetay'),
    path('<slug:slug>/', views.urundetaysayfa, name='urundetay'),

]