from django.contrib import admin

from account.models import Shopper


class ShopAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    search_fields = ['username', ]


admin.site.register(Shopper, ShopAdmin)
