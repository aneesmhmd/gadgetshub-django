from django.db import models
from category.models import Category,Brand
from django.urls import reverse


# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(max_length=200,unique=True)
    images = models.ImageField(upload_to='products')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    price = models.IntegerField()
    stock = models.IntegerField(default=0)
    description = models.TextField(max_length=500,blank=True)
    is_available = models.BooleanField(default=True)  
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug ])

    def __str__(self):
        return self.product_name 