# profiles/forms.py
from django import forms
from .models import Profile, Post

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'description']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']
