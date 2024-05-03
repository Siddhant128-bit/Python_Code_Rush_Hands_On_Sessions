from django.shortcuts import render,redirect
from .models import *
from .form import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

#login required django-so that pahila login garera matraa aoss 


# Create your views here.
@login_required(login_url="/login/")
def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            return redirect('post')
    else:
        form = PostForm()
    posts = Post.objects.all()  # Retrieve all existing posts
    return render(request, 'post/post.html',  {'form': form, 'posts': posts})

def delete_post(request,id):
    queryset=Post.objects.filter(id=id)
    queryset.delete()
    return redirect('post')

def update_post(request,id):
    queryset=Post.objects.get(id=id)
    
    if request.method=="POST":
        post_name = request.POST.get('post_name')
        post_description = request.POST.get('post_description')
        post_image = request.FILES.get('post_image')
        
        queryset.post_name=post_name
        queryset.post_description=post_description
        
        if post_image:
            queryset.post_image=post_image
            
        queryset.save()
        return redirect('post')
    return render(request, 'post/update_post.html',  { 'posts': queryset})

def login_page(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        if not User.objects.filter(username=username).exists():
            messages.error(request,'Invalid username')
            return redirect('/login/')
        
        # basically password encrypted xa so we use django ko autentcate    it return true of false 
        user=authenticate(username=username,password=password)      
        
        if user is None:
            messages.error(request,'Invalid Password')
            return redirect('/login/') 
        #session login save garirakoss pheri login garnaa naparos tesko lagi django ko login banee hunxa
        else:
            login(request,user)
            return redirect('/post/')  

    return render(request,'post/login.html')  


def register_page(request):
    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('email')
        

        
        #check username exist garxa gardaina  we can use 'django message' to flash 
        user=User.objects.filter(username=username)
        
        if user.exists():
            messages.info(request,'Username already taken')
            return redirect('/register/')
        
        user=User.objects.create(
            username=username, 
            first_name=first_name,
            last_name=last_name,
            email=email,         
        )
        
        #to encrypt password
        user.set_password(password)
        user.save()
        messages.info(request,'Account created sucessfully')

        
        return redirect('/register/')
    return render(request,'post/register.html')  

def update_profile(request):
    user = request.user  

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')

        user = request.user
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()
       
       
        
        return redirect('post')  # Assuming you have a URL named 'profile' for viewing user profile       
    return render(request, 'post/update_profile.html',{'user':user})



  
def logout_page(request):
    logout(request)
    return redirect('/login/')
  
# from django.shortcuts import render, redirect
# from .models import Post

# def post(request):
#     if request.method == 'POST':
#         # Extract data from the request
#         post_name = request.POST.get('post_name')
#         post_description = request.POST.get('post_description')
#         post_image = request.FILES.get('post_image')

#         # Create a new Post object and save it to the database
#         Post.objects.create(
#             post_name=post_name,
#             post_description=post_description,
#             post_image=post_image
#         )
#         return redirect('post')
#     else:
#         # Render the form template with an empty form
#         return render(request, 'post/post.html')
