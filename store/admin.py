from django.contrib import admin
from django.http import request
from django.shortcuts import get_object_or_404

from store.models import Product, Order, Cart, Header, Category


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'description', 'category', 'thumbnail')
    # fields = ('name', 'price', 'stock', 'description', 'thumbnail')
    search_fields = ['name', 'price', 'stock', 'category', ]


class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'user')
    # fields = ('username', 'product', 'quantity')
    search_fields = ['product__name', 'user__username']

    # def save_model(self, request, obj, form, change):
    #     super().save_model(request, obj, form, change)
    #
    #     self.add_to_card(request,  obj, )
    # def add_to_card(self, request, slug):
    #     user = request.user
    #     product = get_object_or_404(Product, slug=slug)
    #     cart, _ = Cart.objects.get_or_create(user=user)
    #     order, created = Order.objects.get_or_create(user=user,
    #                                                  product=product)
    #     stock = product.stock
    #     print(stock)
    #
    #     if created:
    #         cart.orders.add(order)
    #         cart.save()
    #     else:
    #         order.quantity += 1
    #         order.save()
    #


class CartAdmin(admin.ModelAdmin):
    list_display = ('user',)
    # fields = ('username', 'product', 'quantity')
    search_fields = ['user__username']


def display_order(self, obj):
    return obj.orders.all()


display_order.short_description = 'orders'


class HeaderAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'picture')
    # fields = ('name', 'price', 'stock', 'description', 'thumbnail')
    search_fields = ['title', ]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name',]


admin.site.register(Product, ProductAdmin)

admin.site.register(Order, OrderAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Header, HeaderAdmin)
admin.site.register(Category, CategoryAdmin)