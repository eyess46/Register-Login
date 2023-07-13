from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from .forms import UserRegistrationForm, AuthenticationForm
from .models import Account
from .models import UserProfile
from .models import User
from .models import ContactForm
from django.utils import timezone 
from django.urls import reverse 




# Create your views here.

def index(request):

    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            account = Account(user=user)
            account.save()
            profile = UserProfile(user=user, email=form.cleaned_data['email'], country=form.cleaned_data['country'], phone_number=form.cleaned_data['phone_number'], btc_address=form.cleaned_data['btc_address'], etherum_address=form.cleaned_data['etherum_address'], profile_picture=form.cleaned_data['profile_picture'])
            if 'profile_picture' in request.FILES:
                profile.profile_picture = request.FILES['profile_picture']
            profile.save()
            messages.success(request, f'Your account has been created! You can now log in.')
            return redirect('login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form })




def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or Password')
            return render(request, 'login.html', {'form': form})

    else:
        form = AuthenticationForm() 
        return render(request, 'login.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('/')


@login_required
def dashboard(request):

    if request.user.is_authenticated:
        user = request.user
        userprofile = UserProfile.objects.get(user=user)
        account = Account.objects.get(user=user)
        if request.method == "POST":
                                
            name = request.POST.get('name') 
            subject = request.POST.get('subject')            
            email = request.POST.get('email')            
            message = request.POST.get('message')            
            image = request.FILES['attachment']      
            
            print(request.FILES)            
            print(name, subject, email, message, image)            
            Contactform.objects.create(name=name, subject=subject, email=email, message=message, image=image)
            messages.success(request, f'Your message is sent and you will get and email urgently.')
            return redirect('dashboard') 

        context = {
            'user': user,
            'userprofile': userprofile,
            'account': account,
        }
        return render(request, 'dashboard.html', context)
    else:
        return redirect('login')





def about(request):

    return render(request, 'about.html')

def innerpage(request):

    return render(request,'innerpage.html') 

def contact(request):

    return render(request, 'contact.html')

def blog(request):

    return render(request, 'blog.html')
