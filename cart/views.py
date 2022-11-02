
#cart
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render,redirect,get_object_or_404
from core.models import*
from.models import*
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def c_id(request):
    ct_id = request.session.session_key
    if not ct_id:
        ct_id = request.session.create()
    return ct_id


def cartdetails(request, tot=0, count=0, c=0,c_item=None):
    try:
        ct = CartList.objects.get(cart_id=c_id(request))
        c_item = CartItems.objects.filter(cart=ct, active=True)
        for i in c_item:
            tot += (i.prod.price * i.quan)
            c = c + 1
        count = tot + 100
    except ObjectDoesNotExist:
        pass

    return render(request, 'cart.html', {'ci': c_item, 't': tot, 'cn': count, 'c': c})


def add_cart(request, product_id):
    pro = products.objects.get(id=product_id)
    try:
        ct = CartList.objects.get(cart_id=c_id(request))
    except CartList.DoesNotExist:
        ct = CartList.objects.create(cart_id=c_id(request))
        ct.save()
    try:
        ct_item = CartItems.objects.get(prod=pro, cart=ct)
        if ct_item.quan < ct_item.prod.stock:
            ct_item.quan += 1
        ct_item.save()
    except CartItems.DoesNotExist:
        ct_item = CartItems.objects.create(prod=pro, quan=1, cart=ct)
        ct_item.save()
    return redirect('cartDetails')


def min_cart(request, product_id):
    ct = CartList.objects.get(cart_id=c_id(request))
    pro = get_object_or_404(products, id=product_id)
    c_item = CartItems.objects.get(prod=pro, cart=ct)
    if c_item.quan > 1:
        c_item.quan -= 1
        c_item.save()
    else:
        c_item.delete()

    return redirect('cartDetails')

def remove(request,product_id):
    ct = CartList.objects.get(cart_id=c_id(request))
    pro = get_object_or_404(products, id=product_id)
    c_item = CartItems.objects.get(prod=pro, cart=ct)
    c_item.delete()
    return redirect('cartDetails')