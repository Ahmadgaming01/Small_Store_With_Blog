from django.contrib import admin
from .models import Product , Brand , Review
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = [ 'name' , 'price' , 'created_date']
    search_fields = ['name','description']
    list_filter = [ 'price','name']
admin.site.register(Product ,ProductAdmin)
admin.site.register(Brand)
admin.site.register(Review)