from django.contrib import admin

from store.models import Product, Order, Cart


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'description', 'thumbnail')
    # fields = ('name', 'price', 'stock', 'description', 'thumbnail')
    search_fields = ['name', ]


class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity')
    # fields = ('username', 'product', 'quantity')
    search_fields = ['product', ]


admin.site.register(Product, ProductAdmin)

admin.site.register(Order, OrderAdmin)
admin.site.register(Cart)
