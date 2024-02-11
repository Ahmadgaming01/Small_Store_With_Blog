from django.shortcuts import render
from .models import Product , Brand , Review
from django.views import generic
# Create your views here.



class ProductList(generic.ListView):
    model = Product
    template_name = 'products/product_list.html'

class ProductDetial(generic.DetailView):
    model = Product
    template_name = 'products/product_detail.html'

class BrandList(generic.ListView):
    model = Brand
    template_name='brands/brand_list.html'

class BrandDetail(generic.ListView):
    model = Brand
    template_name='brands/brand_detail.html'  # One brand has many
    # products so it should be ListView not DetailView

