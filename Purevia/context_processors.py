from urunler.utils import get_cart


def global_context(request):
    cart = get_cart(request)
    total_items = 0

    for item in cart.values():
        if isinstance(item,dict):
            total_items += int(item.get('qty',0) or 0)


    return {
        'cart':cart,
        'cart_total_items':total_items,
        'site_name':'Purevia',
        'brand_color':'#006241',

    }
    


def cart_counter(request):
    cart = request.session.get('cart') or {}
    total_qty = 0

    for _, row in cart.items():

        try:
            total_qty += int(row.get('qty', 1))
        
        except Exception:
            total_qty += 1
    return {'cart_count':total_qty}