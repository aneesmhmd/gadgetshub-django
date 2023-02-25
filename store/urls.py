from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.all_products,name="allProducts"),
    path('<slug:category_slug>/', views.all_products,name="products_by_category"),
    path('<slug:category_slug>/<slug:product_slug>/', views.product_detail,name="product_detail"),
] 