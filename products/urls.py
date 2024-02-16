from django.urls import  path
from .views import ProductList , ProductDetial , BrandList , BrandDetail

urlpatterns = [
    path('' , ProductList.as_view() , name = 'products_list'),
    path('<slug:slug>/detail' , ProductDetial.as_view() , name = 'products_detail'),
    path('brand/' , BrandList.as_view() , name = 'brand_list'),
    path('brand/<slug:slug>/' , BrandDetail.as_view() , name = 'brand_detail'),
]
