from django import forms
from .models import *
  
class PostForm(forms.ModelForm):
  
    class Meta:
        model = Post
        fields = ['post_name', 'post_description','post_image']
        # labels = {
        #     'post_name': 'Title',
        #     'post_description': 'Description',
        #     'post_image': 'Image',
        # }