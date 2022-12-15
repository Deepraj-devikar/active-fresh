from django.contrib import admin
from .models import *

admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Shop)
admin.site.register(ShopImage)
admin.site.register(ProductCategory)
admin.site.register(Cart)
# admin.site.register(WeekDay)
admin.site.register(Area)
admin.site.register(ShopAddress)
admin.site.register(OrderAddress)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ProductReview)