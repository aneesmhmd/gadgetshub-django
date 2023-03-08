from django.shortcuts import render,get_object_or_404
from . models import Product
from category.models import Category,Brand
from carts.models import CartItem

from carts.views import _cart_id
from django.db.models import Q
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.

# Products view
def all_products(request,category_slug=None,brand_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products =Product.objects.filter(category=categories,is_available=True).order_by('id')
        products_count = products.count()

    elif brand_slug != None:
        brands = get_object_or_404(Brand, slug=brand_slug)
        products = Product.objects.filter(brand=brands,is_available=True).order_by('id')
        products_count = products.count
    
    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')
        products_count = products.count()

    paginator = Paginator(products, 4)
    page_number = request.GET.get('page') #capturing the url
    page_obj = paginator.get_page(page_number) #getting page products

    context = {
        'products' : page_obj,
        'count' : products_count
           
    }
    return render (request,'store/all_products.html',context)


# Single product detail
def product_detail(request,category_slug,product_slug):
    in_cart=False
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.get(cart__cart_id=_cart_id(request), product=single_product)
    except Exception as e:
        pass
    
    context = {
        'single_product' : single_product,
        'in_cart' : in_cart,
    }

    return render(request,'store/product_detail.html', context)


# Search
def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            products_count = products.count()

    context = {
        'products' : products,
        'products_count' : products_count,
    }

    return render (request,'store/all_products.html',context)


