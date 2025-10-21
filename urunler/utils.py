


CART_KEY = "cart"

def get_cart(request):

    raw = request.session.get(CART_KEY) or {}
    cart = {}
    changet = False


    for pid, val in raw.items():
        if isinstance(val, dict):
            qty = int(val.get('qty') or val.get('quantity') or 1)
            qty = max(1,qty)

            cart[pid] = {**val, 'qty':qty}

            if 'quantity' in val:
                 changet = True


        else:

            try:
                    qty = max(1, int(val))
            except(TypeError, ValueError):
                    qty = 1

            cart[pid] = {'quantity':qty}
            changet = True


    if changet:
        request.session[CART_KEY] = cart
        request.session.modified = True
    

    return cart









def save_cart(request,cart:dict):
    request.session[CART_KEY] = cart
    request.session.modified = True