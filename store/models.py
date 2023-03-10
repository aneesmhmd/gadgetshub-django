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
    

class VariationManager(models.Manager):
    def ram(self):
        return super(VariationManager,  self).filter(variation_category='ram',is_active=True)
    
    def storage(self):
        return super(VariationManager, self).filter(variation_category='storage',is_active=True)
    
    def colors(self):
        return super(VariationManager, self).filter(vartion_category='color',is_active=True)
    

variation_category_choice = (
    ('color', 'color'),
    ('ram', 'ram'),
    ('storage', 'storage'),
)

class Variation(models.Model):
     product = models.ForeignKey(Product,on_delete=models.CASCADE)
     variation_category = models.CharField(max_length=100,choices=variation_category_choice)
     variation_value = models.CharField(max_length=100)
     is_active = models.BooleanField(default=True)
     created_date = models.DateTimeField(auto_now = True)

     objects = VariationManager()

     def __str__(self):
         return self.variation_value
     
