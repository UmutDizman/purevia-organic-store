from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.templatetags.static import static
# Create your models here.




class Markalar(models.Model):
    isim = models.CharField(max_length=100)
    aciklama = models.TextField( null=True, blank=True)
    seo_title = models.CharField(max_length=100, null=True, blank=True)
    seo_description = models.TextField( null=True, blank=True)
    slug = models.SlugField(max_length=100, null=True, blank=True)
    aktifmi = models.BooleanField(default=True)
    resim = models.ImageField(upload_to="markaresimleri", null=True, blank=True)

    class Meta:
        verbose_name_plural = "Markalar"
        verbose_name = "Markalar"

    def __str__(self):
        return self.isim


class Kategoriler(models.Model):
    isim = models.CharField(max_length=100)
    aciklama = models.TextField(null=True, blank=True)
    seo_title = models.CharField(max_length=100, null=True, blank=True)
    seo_description = models.TextField( null=True, blank=True)
    slug = models.SlugField(max_length=100, null=True, blank=True)
    aktifmi = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Kategoriler"
        verbose_name = "Kategori"

    def __str__(self):
        return self.isim




class Urunler(models.Model):
    isim = models.CharField(max_length=100)
    kullanici = models.ForeignKey(User,on_delete=models.CASCADE)
    marka = models.ForeignKey(Markalar,on_delete=models.CASCADE,blank=True,null=True)
    kategori =models.ForeignKey(Kategoriler,on_delete=models.CASCADE,null=True,blank=True)
    fiyat = models.DecimalField(decimal_places=2, max_digits=10)
    indirimli_fiyat = models.DecimalField(decimal_places=2, max_digits=10,null=True,blank=True)
    kisa_aciklama = models.CharField(max_length=100, null=True, blank=True)
    aciklama=models.TextField(blank=True, null=True)
    seo_title = models.CharField(max_length=100, null=True, blank=True)
    seo_description = models.TextField( null=True, blank=True)
    slug = models.SlugField(max_length=100, null=True, blank=True)
    aktifmi = models.BooleanField(default=True)
    resim = models.ImageField(upload_to="urunresimleri", null=True, blank=True)
    tarih = models.DateTimeField(auto_now_add=True)
    anasayfa = models.BooleanField(default=True)


    @property
    def image_url(self):
        try:
            if self.resim and hasattr(self.resim, "url"):
                return self.resim.url
            
        except Exception:
            pass

        return static("/default_image1.jpg")


    class Meta:
        verbose_name_plural = "Urunler"
        verbose_name = "Urun"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.isim)

        super(Urunler,self).save(*args, **kwargs)
        return self.slug



    def __str__(self):
        return self.isim