from django.db import models

# Create your models here.

class Urunler(models.Model):
    isim = models.CharField(max_length=100)
    fiyat = models.DecimalField(decimal_places=2, max_digits=10)
    kisa_aciklama = models.CharField(max_length=100, null=True, blank=True)
    aciklama=models.TextField(blank=True, null=True)
    seo_title = models.CharField(max_length=100, null=True, blank=True)
    seo_description = models.TextField( null=True, blank=True)
    slug = models.SlugField(max_length=100, null=True, blank=True)
    aktifmi = models.BooleanField(default=True)
    resim = models.ImageField(null=True, blank=True)
    tarih = models.DateTimeField(auto_now_add=True)
    anasayfa = models.BooleanField(default=True)


    class Meta:
        verbose_name_plural = "Urunler"
        verbose_name = "Urun"


    def __str__(self):
        return self.isim


