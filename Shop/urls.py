from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from store.views import index, product_detail, add_to_card, carts
from Shop import settings
from account.views import signup, logout_user, login_user

urlpatterns = [
    path('', index, name='index'),
    path('products/<str:slug>/', product_detail, name='detail'),
    path('products/<str:slug>/add_to_card/', add_to_card, name='add_to_card'),
    path("cart/", carts, name='cart'),
    path("signup/", signup, name='signup'),
    path("login/", login_user, name='login'),
    path("logout/", logout_user, name='logout'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

