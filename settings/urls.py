from django.urls import path
from .views import get_random_post

urlpatterns = [
    path('home/' , get_random_post)
]
