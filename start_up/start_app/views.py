from django.shortcuts import render
from django.http import HttpResponse
from start_app.forms import UserForm, UserProfileForm

from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.

def index(request):
    dict = {'text' : 'Hello world'}
#    return HttpResponse('hello how are you')
    return render(request, 'start_app/index.html', context = dict)

def other(request):
    return render(request, 'start_app/other.html')

def relative(request):
    return render(request, 'start_app/relative_url_templates.html')

def registration(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user =user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit = False)
            profile.user = user
            
            if 'user_img' in request.FILES:
                profile.user_img = request.FILES['user_img']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
            
        
    return render(request, 'start_app/registration.html', context = {'user_form' : user_form,'profile_form' : profile_form, 'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username = username, password = password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account not active')
        else:
            print('Someone tried to login')
            print('username : {} password : {}'.format(username, password))
            return HttpResponse('invalid login credentials')
    else:
        return render(request, 'start_app/login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return  HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse('You are login, nice!')
            
                
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    