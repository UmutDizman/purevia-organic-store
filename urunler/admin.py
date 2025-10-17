from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Urunler,Markalar,Kategoriler


# Register your models here.


class UrunInlineForMarka(admin.TabularInline):
    model = Urunler
    fk_name = 'marka'
    extra = 0
    fields = ['isim','marka','slug','fiyat','aktifmi']
    show_change_link = True

    def has_add_permission(self, request, obj=None):
        return False


class UrunlerInlineForKategoriler(admin.TabularInline):
    model = Urunler
    fk_name = 'kategori'
    extra = 0
    fields = ['isim','kategori','slug','fiyat','aktifmi']
    show_change_link = True

    def has_add_permission(self, request, obj=None):
        return False




class UrunlerAdmin(admin.ModelAdmin):
    list_display = ['isim','fiyat','slug','aktifmi','kullanici']
    list_display_links = ['isim','slug','aktifmi','kullanici']
    search_fields = ['isim','slug','aktifmi','kullanici']


class MarkalarAdmin(admin.ModelAdmin):
    list_display = ['isim','seo_title','slug','aktifmi']
    list_display_links = ['isim','slug','aktifmi']
    search_fields = ['isim','slug','aktifmi']
    inlines = [UrunInlineForMarka]



class KategorilerAdmin(admin.ModelAdmin):
    list_display = ['isim','seo_title','slug','aktifmi']
    list_display_links = ['isim','slug','aktifmi']
    search_fields = ['isim','slug','aktifmi']
    inlines = [UrunlerInlineForKategoriler]





admin.site.register(Kategoriler,KategorilerAdmin)
admin.site.register(Markalar,MarkalarAdmin)
admin.site.register(Urunler,UrunlerAdmin)