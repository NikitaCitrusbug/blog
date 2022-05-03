from django.shortcuts import render
from .forms import SignUpForm , LoginForm

# Create your views here.
def home(request):
    return render(request , 'blog/home.html')
def about(request):
    return render(request , 'blog/about.html')
def contact(request):
    return render(request , 'blog/contact.html')
def dashboard(request):
    return render(request , 'blog/dashboard.html')
def user_logout(request):
    return render(request , 'blog/home.html')
def user_signup(request):
    form = SignUpForm()
    return render(request , 'blog/signup.html' , {'form' : form})
def user_login(request):
    form = LoginForm()
    return render(request , 'blog/login.html', {'form' : form})
