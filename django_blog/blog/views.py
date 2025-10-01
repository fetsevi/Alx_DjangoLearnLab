from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django import forms

# Extending UserCreationForm to add email field
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        
# Registration view

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully! you can now log in")
            return redirect("login")
    else:
        form = RegisterForm()
        return render(request, "blog/register.html", {"form": form})
    

# Profile View (Only for logged-in users)
@login_required
def profile(request):
    if request.method == "POST":
        request.user.email = request.POST.get("email")
        request.user.save()
        messages.success(request, "profile updated successfully!")
        return redirect("profile")
    return render(request, "blog/profile.html", {"user": request.user})
            
