from django.shortcuts import render , redirect
from .models import Post
from django.views import generic
# Create your views here.


class PostListView(generic.ListView):
    model = Post

class PostDetailView(generic.DetailView):
    model=Post

class PostCreateView(generic.CreateView):
    model=Post
    fields =['title','content' , 'image' , 'publich_date' ,'author' ,'tags' ,'likes' , 'dislikes']
    template_name = 'blogs/post_form.html'
    success_url = ''
class PostEditView(generic.UpdateView):
    model=Post
    fields =['title','content' , 'image' , 'publich_date' ,'author' ,'tags' ,'likes' , 'dislikes']
    template_name = 'blogs/post_form.html'
    success_url = ''

class PostDeleteView(generic.DeleteView):
    model=Post
    