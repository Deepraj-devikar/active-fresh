from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .models import *
from django.contrib import messages
from django.db.models import Q

def dairy_shop(request, *args, **kw_args):
    products = Product.objects.all()[0:4]
    slider_products = Product.objects.all()[0:6]
    shops = Shop.objects.all()
    if request.user.is_authenticated:
        cart_count = Cart.objects.filter(user=request.user).count()
    else:
        cart_count = 0
    context = {
        'products': products,
        'slider_products': slider_products,
        'shops': shops,
        'cart_count': cart_count,
    }
    return render(request, 'home.html', context)

def about(request, *args, **kw_args):
    shops = Shop.objects.all()
    slider_products = Product.objects.all()[0:6]
    if request.user.is_authenticated:
        cart_count = Cart.objects.filter(user=request.user).count()
    else:
        cart_count = 0
    context = {
        'shops': shops,
        'slider_products': slider_products,
        'cart_count': cart_count,
    }
    return render(request, 'about.html', context)

def checkout(request, *args, **kw_args):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user)
        total = 0
        for item in cart:
            total = total + item.totalPrice
        opt = {
            'cart': cart,
            'address_types': ADDRESS_TYPES,
            'areas': Area.objects.all(),
            'total': total,
        }
        return render(request, 'checkout.html', opt)
    else:
        opt = {
            'msg': 'not_authenticated',
        }    

def contact(request, *args, **kw_args):
    shops = Shop.objects.all()
    slider_products = Product.objects.all()[0:6]
    if request.user.is_authenticated:
        cart_count = Cart.objects.filter(user=request.user).count()
    else:
        cart_count = 0
    context = {
        'shops': shops,
        'slider_products': slider_products,
        'cart_count': cart_count,
    }
    return render(request, 'contact.html', context)

def customer(request, *args, **kw_args):
    shops = Shop.objects.all()
    slider_products = Product.objects.all()[0:6]
    if request.user.is_authenticated:
        cart_count = Cart.objects.filter(user=request.user).count()
    else:
        cart_count = 0
    context = {
        'shops': shops,
        'slider_products': slider_products,
        'cart_count': cart_count,
    }
    return render(request, 'customer.html')

def payment(request, *args, **kw_args):
    if request.user.is_authenticated:
        if request.method == 'POST':
            OrderAddress.objects.create(
                user = request.user,
                fullName = request.POST.get('full_name'),
                mobile = request.POST.get('mobile'),
                area = Area.objects.get(id=request.POST.get('area')),
                city = request.POST.get('city'),
                addressType = request.POST.get('address_type')
            )
        shops = Shop.objects.all()
        slider_products = Product.objects.all()[0:6]
        if request.user.is_authenticated:
            cart_count = Cart.objects.filter(user=request.user).count()
        else:
            cart_count = 0
        context = {
            'shops': shops,
            'slider_products': slider_products,
            'cart_count': cart_count,
        }
        return render(request, 'payment.html', context)
    else:
        return redirect('index')   

def order(request, *args, **kw_args):
    if request.user.is_authenticated:
        print(request.POST.get('card_number'))
        # if request.POST.get('card_number') != '4242424242424242':
        #     return redirect('index')        
        order = Order.objects.create(
            user = request.user,
            orderAddress = OrderAddress.objects.filter(user=request.user).order_by('-id')[0],
        )
        for item in Cart.objects.filter(user=request.user):
            if item.product.quantity >= item.quantity:
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    unitPrice=item.product.mrp,
                    totalPrice=item.totalPrice,
                )
                Product.objects.filter(
                    id=item.product.id
                ).update(
                    quantity=item.product.quantity-item.quantity
                )
        Cart.objects.filter(user=request.user).delete()
        shops = Shop.objects.all()
        context = {
            'shops': shops,
        }
    return redirect('index')
        

def shop(request, *args, **kw_args):
    try:
        shop = Shop.objects.get(id=kw_args['shop_id'])
    except:
        shop = Shop.objects.get(id=1)
    shops = Shop.objects.all()
    slider_products = Product.objects.all()[0:6]
    if request.user.is_authenticated:
        cart_count = Cart.objects.filter(user=request.user).count()
    else:
        cart_count = 0
    context = {
        'shops': shops,
        'shop' : shop,
        'slider_products': slider_products,
        'cart_count': cart_count,
    }
    return render(request, 'shop.html', context)

def shop_product(request, *args, **kw_args):
    products = Product.objects.filter(productcategory__shop__id=request.POST.get('shop_id'))
    if request.POST.get('search'): 
        search = request.POST.get('search')
        products = products.filter(title__icontains=search)
    else:
        search = ''
    if request.POST.getlist('categories[]'):
        categories = ','.join(request.POST.getlist('categories[]'))
        products = products.filter(productcategory__in=request.POST.getlist('categories[]'))
    else:
        categories = ''
    if request.POST.get('amount'):
        amount = request.POST.get('amount')
    else:
        amount = ''
    if request.POST.getlist('discounts[]'):
        discounts = ','.join(request.POST.getlist('discounts[]'))
    else:
        discounts = ''
    context = {
        'products' : products,
        'search': search,
        'categories': categories,
        'amount': amount,
        'discounts': discounts,
    }
    return render(request, 'shop-product.html', context)

def single(request, *args, **kw_args):
    shops = Shop.objects.all()
    try:
        product = Product.objects.get(id=kw_args['product_id'])
    except:
        product = Product.objects.get(id=1)
    slider_products = Product.objects.all()[0:6]
    if request.user.is_authenticated:
        cart_count = Cart.objects.filter(user=request.user).count()
    else:
        cart_count = 0
    context = {
        'shops': shops,
        'product': product,
        'product_quantity': range(1, product.quantity+1),
        'slider_products': slider_products,
        'cart_count': cart_count,
    }
    return render(request, 'single.html', context)

def not_found(request, *args, **kw_args):
    shops = Shop.objects.all()
    if request.user.is_authenticated:
        cart_count = Cart.objects.filter(user=request.user).count()
    else:
        cart_count = 0
    context = {
        'shops': shops,
        'cart_count': cart_count,
    }
    return render(request, '404.html', context)

def check_login(request, *args, **kw_args):
    return render(request, 'check.html')
    
def my_login(request, *args, **kw_args):
    return render(request, 'my-login.html')
    
def add_to_cart(request, *args, **kw_args):
    if request.method == 'POST':
        if request.user.is_authenticated:
            try:
                product = Product.objects.get(
                    id=request.POST.get('item_id'))
            except:
                opt = {
                    'msg': 'product_not_found',
                }
                print(opt)
                return JsonResponse(opt)
            if product.quantity > 0:
                Cart.objects.create(
                    user = request.user,
                    product = product,
                    unitPrice = product.mrp,
                    totalPrice = product.mrp,
                )
                opt = {
                    'msg': 'product_added',
                    'item_name': product.title,
                }
            else:
                opt = {
                    'msg': 'out_of_stock',
                    'item_name': product.title,
                }    
        else:
            opt = {
                'msg': 'not_authenticated',
            }
    else:
        opt = {
            'msg': 'get_method',
        }
    print(opt)
    return JsonResponse(opt)

def remove_product(request, *args, **kw_args):
    if request.method == 'POST':
        if request.user.is_authenticated:
            Cart.objects.filter(
                id=request.POST.get('item'),
                user=request.user,
            ).delete()
            return redirect('checkout')    
        else:
            opt = {
                'msg': 'not_authenticated',
            }
    else:
        opt = {
            'msg': 'get_method',
        }
    print(opt)
    return JsonResponse(opt)

def change_qty(request, *args, **kw_args):
    if request.method == 'POST':
        if request.user.is_authenticated:
            cart = Cart.objects.get(
                id=request.POST.get('item'),
                user=request.user,
            )
            Cart.objects.filter(
                id=request.POST.get('item'),
                user=request.user,
            ).update(
                quantity=int(int(cart.quantity)+int(request.POST.get('qty'))),
                totalPrice=cart.totalPrice+int(request.POST.get('qty'))*cart.product.mrp,
            )
            return redirect('checkout')    
        else:
            opt = {
                'msg': 'not_authenticated',
            }
    else:
        opt = {
            'msg': 'get_method',
        }
    print(opt)
    return JsonResponse(opt)




def add_product(request, *args, **kw_args):
    if request.user.is_authenticated:
        try:
            shop = Shop.objects.get(user=request.user.id)
            if request.method == 'POST':
                product = Product.objects.create(
                    title = request.POST.get('title'),
                    mrp = request.POST.get('mrp'),
                    rate = request.POST.get('rate'),
                    discount = request.POST.get('discount'),
                    quantity = request.POST.get('qty'),
                    description = request.POST.get('desc'),
                    information = request.POST.get('info'),
                )
                for opt in request.POST.getlist('opts[]'):
                    opt_product = Product.objects.get(id=opt)
                    product.options.add(opt_product)
                    opt_product.options.add(product)
                ProductCategory.objects.get(id=request.POST.get('category')).products.add(product)
                for img in request.FILES.getlist('imgs[]'):
                    ProductImage(
                        product = product,
                        image = img
                    ).save()
            products = shop.products
            product_categories = shop.productCategories
            context = {
                'products': products,
                'product_categories': product_categories
            }
            return render(request, 'seller/add-product.html', context)
        except:
            return redirect('/seller-activation/')
    else:
        return redirect('seller-login')

def add_product_ctaegory(request, *args, **kw_args):
    if request.user.is_authenticated:
        try:
            shop = Shop.objects.get(user=request.user.id)
            if request.method == 'POST':
                ProductCategory(
                    name = request.POST.get('name'),
                    shop = shop,
                    image = request.FILES.get('img')
                ).save()
                print(request.POST.get('img'))
            return render(request, 'seller/add-product-ctegory.html')
        except:
            return redirect('seller-activation')
    else:
        return redirect('seller-login')

def seller_activation(request, *args, **kw_args):
    if request.user.is_authenticated:
        try:
            Shop.objects.get(user=request.user.id)
            return redirect('seller-orders')
        except:
            if request.method == 'POST':
                shop = Shop.objects.create(
                    user = request.user,
                    name = request.POST.get('shop'),
                    openingTime = request.POST.get('start_time'),
                    closingTime = request.POST.get('end_time')
                )
                for off_day in request.POST.getlist('off_days[]'):
                    shop.offDays.add(WeekDay.objects.get(id=off_day))
                return redirect('seller-orders')
            else:
                weekDays = WeekDay.objects.all()
                context = {
                    'weekdays': weekDays
                }
                return render(request, 'seller/activation.html', context)
    else:
        return redirect('seller-login')
        
    
    
def seller_login(request, *args, **kw_args):
    if request.user.is_authenticated:
        try:
            Shop.objects.get(user=request.user.id)
            return redirect('seller-orders')
        except:
            return render(request, 'seller/activation.html', context)
    else:
        return render(request, 'seller/login.html')

def sale_search(request, *args, **kw_args):
    search_inp = request.GET.get('search_inp')
    shops = Shop.objects.all()
    slider_products = Product.objects.all()[0:6]
    search_shops = Shop.objects.filter(
        Q(name__icontains=search_inp) | 
        Q(shopaddress__area__name__icontains=search_inp) |
        Q(shopaddress__area__nearTo__name__icontains=search_inp) |
        Q(productcategory__name__icontains=search_inp)
    )
    search_products = Product.objects.filter(
        Q(title__icontains=search_inp) | 
        Q(productcategory__name__icontains=search_inp)
    )
    context = {
        'search_shops': search_shops,
        'search_products': search_products,
        'shops': shops,
        'slider_products': slider_products,
    }
    return render(request, 'search.html', context)


def check_location(request, *args, **kw_args):
    check_inp = request.POST.get('check_inp')
    product_id = request.POST.get('product_id')
    try:
        product = Product.objects.filter(
            Q(productcategory__shop__shopaddress__area__name__icontains=check_inp) |
            Q(productcategory__shop__shopaddress__area__nearTo__name__icontains=check_inp)
        ).get(id=product_id)
    except:
        return JsonResponse({'result': '0'}) 
    return JsonResponse({'result': '1'})
    
def review(request, *args, **kw_args):
    product_id = request.POST.get('product_id')
    message = request.POST.get('message')
    ProductReview.objects.create(
        product=Product.objects.get(id=product_id),
        user=request.user,
        message=message,
    )
    return redirect('single', product_id)

def seller_order(request, *args, **kw_args):
    if request.user.is_authenticated:
        try:
            shop = Shop.objects.get(user=request.user.id)
        except:
            return redirect('seller-activation')
        order_items = OrderItem.objects.filter(
            product__productcategory__shop__user = request.user
        )
        context = {
            'order_items': order_items
        }
        return render(request, 'seller/orders.html', context)
    else:
        return redirect('seller-login')

    
def seller_carted(request, *args, **kw_args):
    if request.user.is_authenticated:
        try:
            shop = Shop.objects.get(user=request.user.id)
        except:
            return redirect('seller-activation')
        cart = Cart.objects.filter(
            product__productcategory__shop__user = request.user,
        )
        context = {
            'cart': cart,
        }
        return render(request, 'seller/carted.html', context)
    else:
        return redirect('seller-login')


def seller_product(request, *args, **kw_args):
    if request.user.is_authenticated:
        try:
            shop = Shop.objects.get(user=request.user.id)
        except:
            return redirect('seller-activation')
        products = Product.objects.filter(
            productcategory__shop__user = request.user
        )
        context = {
            'products': products
        }
        return render(request, 'seller/products.html', context)
    else:
        return redirect('seller-login')

def seller_category(request, *args, **kw_args):
    if request.user.is_authenticated:
        try:
            shop = Shop.objects.get(user=request.user.id)
        except:
            return redirect('seller-activation')
        product_categories = ProductCategory.objects.filter(
            shop__user = request.user
        )
        context = {
            'product_categories': product_categories
        }
        return render(request, 'seller/product-categories.html', context)
    else:
        return redirect('seller-login')


def shop_address(request, *args, **kw_args):
    if request.user.is_authenticated:
        try:
            shop = Shop.objects.get(user=request.user.id)
        except:
            return redirect('seller-activation')
        if request.method == 'POST':
            ShopAddress.objects.filter(
                shop=shop,
            ).delete()
            ShopAddress.objects.create(
                shop=shop,
                area=Area.objects.get(id=request.POST.get('area')),
                details=request.POST.get('address'),
            )
            return redirect('seller-orders')    
        else:
            areas = Area.objects.all()
            context = {
                'areas': areas,
            }
            return render(request, 'seller/shop-address.html', context)
    else:
        return redirect('seller-login')


def options(request, *args, **kw_args):
    return render(request, 'options.html')

def my_signup(request, *args, **kw_args):
    products = Product.objects.all()[0:4]
    slider_products = Product.objects.all()[0:6]
    shops = Shop.objects.all()
    if request.user.is_authenticated:
        cart_count = Cart.objects.filter(user=request.user).count()
    else:
        cart_count = 0
    context = {
        'products': products,
        'slider_products': slider_products,
        'shops': shops,
        'cart_count': cart_count,
    }
    return render(request, 'home2.html', context)

#https://developers.google.com/maps/documentation/javascript/examples/map-geolocation#maps_map_geolocation-javascript