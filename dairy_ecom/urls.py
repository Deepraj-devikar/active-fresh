"""dairy_ecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import shop.views as shop_view
import connect.views as connect_view
from django.conf import settings
from django.conf.urls.static import static


my_static = static(settings.STATIC_URL, document_root=settings.STATIC_DIR)
my_media = static(settings.MEDIA_URL, document_root=settings.MEDIA_DIR)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', shop_view.dairy_shop, name="index"),
    path('about', shop_view.about, name="about"),
    path('checkout', shop_view.checkout, name="checkout"),
    path('contact', shop_view.contact, name="contact"),
    path('customer', shop_view.customer, name="customer"),
    path('payment', shop_view.payment, name="payment"),
    path('order', shop_view.order, name="order"),
    path('shop', shop_view.shop, name="shop"),
    path('shop/<int:shop_id>', shop_view.shop, name="shop"),
    path('shop-product', shop_view.shop_product, name="shop-product"),
    path('product', shop_view.single, name="single"),
    path('product/<int:product_id>', shop_view.single, name="single"),
    path('accounts/', include('allauth.urls')),
    path('check/', shop_view.check_login),
    path('my-login/', shop_view.my_login),
    path('add-product/', shop_view.add_product, name='add-product'),
    path('remove-product/', shop_view.remove_product, name='remove-product'),
    path('change-qty/', shop_view.change_qty, name='change-qty'),
    path('add-product-category/', shop_view.add_product_ctaegory, name='add-product-category'),
    path('seller-activation/', shop_view.seller_activation, name="seller-activation"),
    path('seller-login/', shop_view.seller_login, name="seller-login"),
    path('sale-search', shop_view.sale_search, name="sale-search"),
    path('add-to-cart', shop_view.add_to_cart, name="add-to-cart"),
    path('seller-orders', shop_view.seller_order, name='seller-orders'),
    path('seller-carted', shop_view.seller_carted, name='seller-carted'),
    path('seller-products', shop_view.seller_product, name='seller-products'),
    path('seller-categories', shop_view.seller_category, name='seller-categories'),
    path('shop-address', shop_view.shop_address, name='shop-address'),
    path('review', shop_view.review, name="review"),
    path('save-info', connect_view.save_info, name="save-info"),
    path('accounts/profile/', shop_view.options),
    
    path('check-location', shop_view.check_location, name="check-location"),
    path('<url_content>', shop_view.not_found),
] + my_static + my_media

#    path('accounts/signup/', shop_view.my_signup),