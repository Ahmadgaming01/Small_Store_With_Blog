from django.shortcuts import render
from blogs.models import Post
# Create your views here.


def get_random_post(request):
    data = Post.objects.filter()[:3]
    context = {'data':data}
    return render(request , 'settings/home.html' ,context)

