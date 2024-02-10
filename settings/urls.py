from django.urls import path
from .views import get_random_post , about_us , contact_us
app_name = 'settings'
urlpatterns = [
    path('home/' , get_random_post , name = 'home_page'),
    path('contact_us/' , contact_us , name = 'contact_us'),
    
]
