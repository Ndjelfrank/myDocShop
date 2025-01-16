from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, resolvers
from django.core.paginator import Paginator
from store.models import Product, Cart, Order, Header, Category
from django.db.models import Q


def index(request):
    #products = Product.objects.filter(Category=Category.name)
    elements = Header.objects.all()
    #categories = Category.objects.prefetch_related('products').all()

    categories = Category.objects.all()
    paginator = Paginator(categories, 1)
    page_number = request.GET.get("page")
    page_object = paginator.get_page(page_number)

    category_product = {}
    for category in categories:
        category_product[category] = Product.objects.filter(category=category)[:4]

    item_name = request.GET.get('item-name')
    if item_name != "" and item_name is not None:
        category_product = Product.objects.filter(name__icontains=item_name)

    return render(request, "store/index.html",
                  context={"category_product": category_product, "elements": elements, "page_object": page_object})


def search(request):
    products = Product.objects.all()
    item_name = request.GET.get('item-name')
    if item_name != "" and item_name is not None:
        products = Product.objects.filter(Q(name__icontains=item_name) |
                                          Q(price__icontains=item_name) |
                                          Q(description__icontains=item_name) |
                                          Q(thumbnail__icontains=item_name))
    else:
        pass

    product_number = products.count()
    message = f'{product_number} résultats :'
    if product_number == 1 or 0:
        message = f'{product_number} résultat :'

    context = {"product": products,
               "item": item_name,
               "message": message}
    return render(request, "store/search.html", context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, "store/detail.html", context={"product": product})
    # return HttpResponse(f" {product.name} <br>"
    #     f" {product.price} <br>"
    #                     f"{product.thumbnail.url}")


# def home(request):
#     current_url = request.path
#     return render(request, "store/index.html", context={"current_url": current_url})

# @login_required(login_url='login')
def add_to_cart_detail(request, slug):
    # actual_page = request.path
    users = request.user
    product = get_object_or_404(Product, slug=slug)
    cart, _ = Cart.objects.get_or_create(user=users)
    order, created = Order.objects.get_or_create(user=users,
                                                 product=product)
    stock = product.stock
    print(stock)

    if created:
        cart.orders.add(order)
        cart.save()
    else:
        order.quantity += 1
        order.save()

    return redirect(reverse('detail', kwargs={'slug': slug}))


def add_to_cart_index(request, slug):
    users = request.user
    product = get_object_or_404(Product, slug=slug)
    cart, _ = Cart.objects.get_or_create(user=users)
    order, created = Order.objects.get_or_create(user=users,
                                                 product=product)
    stock = product.stock
    print(stock)

    if created:
        cart.orders.add(order)
        cart.save()
    else:
        order.quantity += 1
        order.save()

    return redirect(reverse('index', kwargs={'slug': slug}))


# def connected_or_not(request, slug):
#     if not request.user.is_authenticated:
#         return redirect('login')
#     elif request.user.is_authenticated:
#         add_to_card(request, slug=slug)
#     else:
#         pass

@login_required(login_url='login')
def carts(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    # cart = get_object_or_404(Cart, user=request.user)
    print(request.user, cart.orders.all())
    return render(request, 'store/cart.html', context={'orders': cart.orders.all()})


@login_required(login_url='login')
def delete_order(request, slug):
    user = request.user
    cart = get_object_or_404(Cart, user=user)
    product = Product.objects.get(slug=slug)
    order = Order.objects.filter(user=user, product=product)
    order.delete()
    # del_item = cart.orders.get(order)
    # del_item.delete()

    # user = request.user
    # #cart = request.user.cart
    # product = get_object_or_404(Product, slug=slug)
    # order = Order.objects.filter(user=user, product=product).first()
    #
    # if order:
    #     Cart.objects.filter(user=user, orders=order).delete()
    #     #cart.save()
    #     order.delete()

    return redirect('cart')


@login_required(login_url='login')
def delete_cart(request):
    cart = request.user.cart
    if cart:
        cart.orders.all().delete()
        cart.delete()

    return redirect('index')


def display_header(request):
    elements = Header.objects.all()

    return render(request, "store/index.html", context={"elements": elements})
