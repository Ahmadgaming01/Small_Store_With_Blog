from django.db import models
from django.utils import  timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Product(models.Model):
    name =  models.CharField(max_length=200)
    description = models.TextField(max_length = 15000)
    image = models.ImageField(upload_to= 'images')
    price = models.FloatField(default = 0)
    created_date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User , related_name = 'product_user' , on_delete = models.Case)
    def __str__(self):
        self.name 

class Brand(models.Model):
    product = models.ForeignKey(Product , related_name = 'brand_product',on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to= 'brands')
    def __str__(self):
        return self.name
    
class Review(models.Model):
    title = models.CharField(max_length = 200)
    review = models.TextField(max_length = 10000)
    image = models.ImageField(upload_to='review')
    rating = models.IntegerField( default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    user= models.ForeignKey(User , related_name = 'review_user' ,on_delete=models.CASCADE)
    date= models.DateTimeField(default = timezone.now)
    Product = models.ForeignKey(Product , related_name = 'reviews' ,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    