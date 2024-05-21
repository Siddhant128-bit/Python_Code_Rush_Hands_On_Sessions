# profiles/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile, Post
from .forms import ProfileForm, PostForm

@login_required
def profile(request):
    user_profile, created = Profile.objects.get_or_create(user=request.user)
    posts = Post.objects.filter(user=request.user).order_by('-created_at')
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile')
    else:
        profile_form = ProfileForm(instance=user_profile)
    post_form = PostForm()
    return render(request, 'profiles/profile.html', {'profile_form': profile_form, 'post_form': post_form, 'posts': posts})

@login_required
def create_post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = request.user
            post.save()
    return redirect('profile')
