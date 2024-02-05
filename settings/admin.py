from django.contrib import admin
from .models import Company
# Register your models here.
class AdminCompany (admin.ModelAdmin):
    list_display = ('name', 'address')


admin.site.register(Company)

