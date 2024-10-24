from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from store.models import Product, Cart, Order


def index(request):
    products = Product.objects.all()

    return render(request, "store/index.html", context={"product": products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, "store/detail.html", context={"product": product})
    # return HttpResponse(f" {product.name} <br>"
    #     f" {product.price} <br>"
    #                     f"{product.thumbnail.url}")


# def home(request):
#     current_url = request.path
#     return render(request, "store/index.html", context={"current_url": current_url})


def add_to_card(request, slug):
    user = request.user
    product = get_object_or_404(Product, slug=slug)
    cart, _ = Cart.objects.get_or_create(user=user)
    order, created = Order.objects.get_or_create(user=user,
                                                 product=product)

    if created:
        cart.orders.add(order)
        cart.save()
    else:
        order.quantity += 1
        order.save()
    return redirect(reverse('detail', kwargs={'slug': slug}))


def carts(request):
    cart = get_object_or_404(Cart, user=request.user)

    return render(request,'store/cart.html', context={'orders': cart.orders.all()})
