from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    cat_name = models.CharField(max_length=50,unique=True)
    slug = models.SlugField(max_length=100,unique=True)
    description = models.TextField(max_length=255,blank=True)
    cat_image = models.ImageField(upload_to='categories',blank=True)

    class Meta():
        verbose_name = ('category')
        verbose_name_plural = ('categories')

    def get_url(self):
        return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        return self.cat_name

class Brand(models.Model):
    brand_name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(max_length=100,unique=True)

    def get_url(self):
        return reverse('products_by_brand', args=[self.slug])

    def __str__(self):
        return self.brand_name
        