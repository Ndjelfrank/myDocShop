from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from store.views import index, product_detail, carts, delete_order, delete_cart, add_to_cart_detail, add_to_cart_index, \
    search
from Shop import settings
from account.views import signup, logout_user, login_user

urlpatterns = [
                  path('', index, name='index'),
                  # path('/head', display_header, name='head'),
                  path('products/<str:slug>/', product_detail, name='detail'),
                  path('products/<str:slug>/add_to_cart/', add_to_cart_detail, name='add_to_cart'),
                  path('products/<str:slug>/add_to_cart/', add_to_cart_index, name='add_to_cart_index'),
                  path("products/<str:slug>/delete/", delete_order, name='delete_order'),
                  path("product/cart/delete", delete_cart, name='delete_cart'),
                  path("cart/", carts, name='cart'),
                  path("search/", search, name='search'),
                  path("signup/", signup, name='signup'),
                  path("login/", login_user, name='login'),
                  path("logout/", logout_user, name='logout'),
                  path('admin/', admin.site.urls),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
