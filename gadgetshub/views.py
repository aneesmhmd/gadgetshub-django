from django.shortcuts import render
from category.models import Category
from store.models import Product

def home(request):
    context = {
        'categories' : Category.objects.all(),
        'products' : Product.objects.all().filter(is_available=True)
    }
    return render(request, 'user_side/index.html',context)