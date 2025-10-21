from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Urunler,Kategoriler
from .utils import get_cart, save_cart
from decimal import Decimal
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login

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




#user

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, "Hesabınız oluşturuldu, hoş geldin!")

            next_url = request.GET.get("next") or request.POST.get("next")
            return redirect(next_url or "purevia:index")
        
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form":form})




#cart görünümleri

def cart_detail(request):
    cart = get_cart(request)
    items = []
    total = Decimal('0')


    for pid, row in list(cart.items()):
        urun = get_object_or_404(Urunler, id=int(pid))

        if not urun.aktifmi:
            cart.pop(str(urun.id), None)
            continue


        qty = int(row.get('qty',1))

        price = urun.indirimli_fiyat or urun.fiyat
        line_total = qty * price
        total += line_total
        
        


        items.append({
            'urun':urun,
            'qty':qty,
            'price':price,
            'line_total':line_total,


        })


    save_cart(request, cart)

    return render(request,'cart.html', {'items':items, 'total':total})
    



def cart_add(request):

    if request.method != 'POST':
        return redirect("/")
        


    product_id = request.POST.get("product_id")
    qty = int(request.POST.get("qty",1))   


    urun = get_object_or_404(Urunler, id=product_id, aktifmi = True)


    cart = get_cart(request)
    key = str(urun.id)


    image_url = urun.image_url



    row = cart.get(key,{
        'qty':0,
        'name':urun.isim,
        'price':float(urun.indirimli_fiyat or urun.fiyat),
        'image':image_url,
        'slug':urun.slug,
    })


    row['qty'] = int(row.get('qty', 0)) + qty
    cart[key] = row
    save_cart(request, cart)



    messages.success(request, f"'{urun.isim}' sepete eklendi.")
    return redirect("purevia:cart_detail")        
    




def cart_remove(request, product_id):
    cart = get_cart(request)
    cart.pop(str(product_id), None)
    save_cart(request, cart)
    messages.info(request, "Ürün sepetten çıkarıldı.")
    return redirect("purevia:cart_detail")






def cart_update(request):
    if request.method == 'POST':
        cart = get_cart(request)
        new_cart = {}


        for key, val in request.POST.items():
            if key.startswith('qty_'):
                pid = key.split('_',1)[1]

                try:
                    qty = max(1,int(val))
                except ValueError:
                    qty = 1
                    
                old = cart.get(pid, {})
                new_cart[pid] = {**old, 'qty': qty}

        save_cart(request, new_cart)
        messages.success(request, 'Sepet güncellendi.')
    
    return redirect('purevia:cart_detail')




@login_required(login_url='/accounts/login/')
def checkout(request):
    cart = get_cart(request)
    if not cart:
        messages.warning(request, 'Sepetin boş!')
        return redirect('purevia:index')
    
    return render(request, 'checkout.html')