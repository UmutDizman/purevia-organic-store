from django.contrib import admin
from .models import Urunler


# Register your models here.


class UrunlerAdmin(admin.ModelAdmin):
    list_display = ['isim','fiyat','slug','aktifmi']
    list_display_links = ['isim','slug','aktifmi']
    search_fields = ['isim','slug','aktifmi']


admin.site.register(Urunler,UrunlerAdmin)