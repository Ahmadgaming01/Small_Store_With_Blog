from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 200)
    image = models.ImageField(upload_to="images")
    content = models.TextField(max_length = 15000)
    publich_date = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User , related_name = 'user_post' , on_delete = models.CASCADE)
    tags = TaggableManager()
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)
    dislikes = models.ManyToManyField(User, related_name='post_dislikes', blank=True)
    def __str__(self):
        return self.title