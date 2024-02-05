from django.db import models

# Create your models here.



class Company (models.Model):
    name = models.CharField (max_length = 100)
    address = models.CharField(max_length = 250)
    logo = models.ImageField(upload_to='images')
    phone = models.CharField(max_length =  30, blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name
    