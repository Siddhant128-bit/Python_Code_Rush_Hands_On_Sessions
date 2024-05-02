from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    post_name=models.CharField(max_length=100)
    post_description=models.TextField()
    post_image=models.ImageField( upload_to="post_images/")
        

def __str__(self):
    return self.title