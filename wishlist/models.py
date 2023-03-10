from django.db import models
from store.models import Product, Variation

# Create your models here.

class Wishlist(models.Model):
    wishlist_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.wishlist_id)
    

class WishlistItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variations = models.ManyToManyField(Variation, blank=True)
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.product
