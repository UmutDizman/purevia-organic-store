
from django.urls import path
from . import views

app_name = 'purevia'



urlpatterns = [
    path("", views.index, name="index"),


    path('sepet/',views.cart_detail,name='cart_detail'),
    path('sepet/ekle/',views.cart_add, name='cart_add'),
    path('sepet/sil/<int:product_id>/',views.cart_remove, name='cart_remove'),
    path('sepet/guncelle/',views.cart_update,name='cart_update'),

    path('checkout/',views.checkout,name='checkout'),

    path('kategori/<slug:slug>/', views.kategoridetay, name='kategoridetay'),
    path('urun/<slug:slug>/', views.urundetaysayfa, name='urundetay'),


    
    


]