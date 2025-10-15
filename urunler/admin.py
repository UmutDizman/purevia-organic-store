from django.contrib import admin
from .models import Urunler,Markalar


# Register your models here.


class UrunlerAdmin(admin.ModelAdmin):
    list_display = ['isim','fiyat','slug','aktifmi','kullanici']
    list_display_links = ['isim','slug','aktifmi','kullanici']
    search_fields = ['isim','slug','aktifmi','kullanici']


class MarkalarAdmin(admin.ModelAdmin):
    list_display = ['isim','slug','aktifmi','resim']
    list_display_links = ['isim','slug','aktifmi']
    search_fields = ['isim','slug','aktifmi']


admin.site.register(Markalar,MarkalarAdmin)
admin.site.register(Urunler,UrunlerAdmin)