from .views import PostListView , PostDetailView , PostCreateView , PostEditView , PostDeleteView
from django.urls import path
app_name = 'blogs'
urlpatterns=[
    path('' , PostListView.as_view() , name = 'post_list'),
    path('post/create/' , PostCreateView.as_view() , name='post_create'),
    path('post/<int:pk>/update' , PostEditView.as_view() , name= 'post_edit'),
    path('post/<int:pk>/detail' , PostDetailView.as_view() , name='post_detail'),
    path('post/<int:pk>/delete' , PostDeleteView.as_view() , name='post_delete'),


]
