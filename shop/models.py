from django.db import models
from django.contrib.auth.models import User 

class Product(models.Model):
    title = models.CharField(max_length = 50, default="")
    mrp = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    rate = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    discount = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    quantity = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    description = models.TextField()
    information = models.TextField()
    options = models.ManyToManyField('self', blank=True)

    def images(self):
        return ProductImage.objects.filter(product=self) 

    def reviews(self):
        return ProductReview.objects.filter(product=self)

    def __str__(self):
        return self.title

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_image', max_length=100)

    def __str__(self):
        return self.product.title + " image"             

class WeekDay(models.Model):
    name = models.CharField(max_length = 20)
    
    def __str__(self):
        return self.name

class Shop(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 50)
    oneLine = models.CharField(max_length = 100, null=True, blank=True)
    shortDescription = models.TextField(null=True, blank=True)
    longDescription = models.TextField(null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)
    openingTime = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    closingTime = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    offDays = models.ManyToManyField(WeekDay)
    
    def productCategories(self):
        return ProductCategory.objects.filter(shop=self)

    def products(self):
        return Product.objects.filter(productcategory__shop=self)
        
    def images(self):
        return ShopImage.objects.filter(shop=self)

    def __str__(self):
        return self.name

class ShopImage(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='shop_image', max_length=100)  

    def __str__(self):
        return self.shop.name + " image"

class ProductCategory(models.Model):
    name = models.CharField(max_length = 50)
    products = models.ManyToManyField(Product)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_category_image', max_length=100)
    
    def __str__(self):
        return self.name + " ( " + self.shop.name + " ) "    

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    unitPrice = models.DecimalField(max_digits=20, decimal_places=2)
    totalPrice = models.DecimalField(max_digits=50, decimal_places=2)

class Area(models.Model):
    name = models.CharField(max_length = 50)
    nearTo = models.ManyToManyField('self', blank=True)
    
    def __str__(self):
        return self.name

class ShopAddress(models.Model):
    shop = models.OneToOneField(Shop, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    details = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.shop.name + '( ' + self.area.name + ' )'

ADDRESS_TYPES =(
    ("O", "Office"),
    ("H", "Home"),
    ("C", "Commercial"),
)

class OrderAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fullName = models.CharField(max_length = 100)
    mobile = models.CharField(max_length = 50)
    area = models.OneToOneField(Area, on_delete=models.CASCADE)
    city = models.CharField(max_length = 50)
    addressType = models.CharField(max_length = 5, choices=ADDRESS_TYPES)

    def __str__(self):
        return self.area.name 

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    orderAddress = models.ForeignKey(OrderAddress, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + '( ' + self.orderAddress.area.name + ' )'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    unitPrice = models.DecimalField(max_digits=20, decimal_places=2)
    totalPrice = models.DecimalField(max_digits=50, decimal_places=2)    

    def __str__(self):
        return self.order.user.username+'( '+self.product.title+' * '+str(self.quantity)+' ) '+str(self.totalPrice)

class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    
    
