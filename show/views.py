from django.shortcuts import render
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from recombee_api_client.api_client import RecombeeClient
from recombee_api_client.exceptions import APIException
from recombee_api_client.api_requests import *

client = RecombeeClient('tvseries', 'Xfp4Upkxyb4DpUC99e2wjU3REiOwcbibJnCYqFq97Pt8uAZhwi2aVD1SPzzgEofM')

def homepage(request):
    return render(request, './show/index.html')


def login(request):
    if request.user.is_authenticated:
        redirect_url = '/profile/' + str(request.user.id)
        return HttpResponseRedirect(redirect_url)
    else:
        if request.method == 'POST':
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    redirect_url = '/profile/' + str(user.id)
                    auth_login(request, user)
                    return HttpResponseRedirect(redirect_url)
                else:
                    error = 'Your account is disabled.'
                    return render(request, './show/login.html', {'error': error})
            else:
                error = 'Incorrect Username or Password'
                return render(request, './show/login.html', {'error': error})
        else:
            return render(request, './show/login.html', {})


def logout(request):
    auth_logout(request)
    return redirect(reverse('show:login'))


def register(request):
    if request.user.is_authenticated:
        redirect_url = '/profile/' + str(request.user.id)
        return HttpResponseRedirect(redirect_url)
    else:
        if request.method == 'POST':
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            email = request.POST.get('email', '')
            first_name = request.POST.get('fname', '')
            last_name = request.POST.get('lname', '')

            if User.objects.filter(username=username).exists():
                error = 'The Sap_id is already in use by another account.'
                return render(request, './show/register.html', {'error': error})

            else:
                user = User.objects.create_user(username=username, email=email,first_name=first_name,last_name=last_name)
                user.set_password(password)
                user.save()
                profile = UserProfile.objects.create(user=user)
                profile.save()
                redirect_url = '/profile/' + str(user.id)
                auth_login(request, user)
                return HttpResponseRedirect(redirect_url)
        else:
            return render(request, './show/register.html')


@login_required
def profile(request,id):
    id = int(id)
    if id == request.user.id:
        if request.method == 'POST':
            username = request.POST.get('username', '')
            email = request.POST.get('email', '')
            first_name = request.POST.get('fname', '')
            last_name = request.POST.get('lname', '')
            gender = request.POST.get('gender', '')
            interests = request.POST.get('interests', '')
            user = User.objects.get(id=id)
            profile = UserProfile.objects.get(user=user)
            user.username = username
            user.email = email
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            profile.gender = gender
            profile.interests = interests
            profile.save()
            return render(request, './show/profile.html',{'profile':profile,'user':user})
        else:
            user = User.objects.get(id=id)
            profile = UserProfile.objects.get(user=user)
            return render(request, './show/profile.html',{'profile':profile,'user':user})
    else:
        user = request.user
        profile = UserProfile.objects.get(user=user)
        redirect_url = '/profile/' + str(user.id)
        return HttpResponseRedirect(redirect_url)
