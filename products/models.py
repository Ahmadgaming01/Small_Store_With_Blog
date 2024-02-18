from typing import Iterable
from django.db import models
from django.utils import  timezone
from django.utils.translation import  gettext_lazy as _
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify
# Create your models here.

class Product(models.Model):
    name =  models.CharField(_("name"),max_length=200)
    description = models.TextField( _('Description') ,max_length = 15000)
    image = models.ImageField(_('Image'),upload_to= 'images')
    price = models.FloatField(_('Price'),default = 0)
    created_date = models.DateTimeField(default=timezone.now)
    brand = models.ForeignKey('Brand' , verbose_name = _('Brand') ,  related_name = 'product_brand',on_delete=models.CASCADE)
    user = models.ForeignKey(User , verbose_name = _('User') ,  related_name = 'product_user' , on_delete = models.Case)
    slug = models.SlugField(blank =True , null = True )
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Product , self).save(*args, **kwargs)
        
        
    
    def __str__(self):
        return self.name 

class Brand(models.Model):
    
    name = models.CharField(_('Name') ,max_length=50)
    image = models.ImageField( _('Image') ,upload_to= 'brands')
    slug = models.SlugField(blank = True , null = True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Brand , self).save(*args, **kwargs)
        
    def __str__(self):
        return self.name
    
class Review(models.Model):
    title = models.CharField( _('Title') ,max_length = 200)
    review = models.TextField(_('Review') ,max_length = 10000)
    image = models.ImageField(_('Image') ,upload_to='review')
    rating = models.IntegerField( _('Rate') , default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    user= models.ForeignKey(User , verbose_name = _('User') ,related_name = 'review_user' ,on_delete=models.CASCADE)
    date= models.DateTimeField( _('Publish Date'),default = timezone.now)
    Product = models.ForeignKey(Product ,verbose_name = _('Product'), related_name = 'reviews' ,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    