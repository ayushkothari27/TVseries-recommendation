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
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView

client = RecombeeClient('tvseries', 'IG1t5vSWYgpJvClpbJZUn29oqnCu6QnIHoJdm9u5dRLom47i0WrpWrNKcZ9om21x')

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


@login_required
def watchlist(request,id):
    id = int(id)
    if id == request.user.id:
        user = User.objects.get(id=id)
        profile = UserProfile.objects.get(user=user)
        watch_list = Watchlist.objects.filter(user=profile)
        return render(request, './show/watchlist.html',{'watch_list':watch_list,'id':id})
    else:
        user = request.user
        profile = UserProfile.objects.get(user=user)
        redirect_url = '/watchlist/' + str(user.id)
        return HttpResponseRedirect(redirect_url)

class WatchlistDeleteView(DeleteView):
    login_url = '/login/'
    model = Watchlist
    success_url = '/watchlist/'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        success_url = success_url + str(self.request.user.id)
        print(self.object)
        self.object.delete()
        return HttpResponseRedirect(success_url)

@login_required
def WatchlistCompView(request,id):
    user = request.user
    obj = Watchlist.objects.get(id=id)
    obj.status = "Completed"
    obj.percent = 100
    obj.save()
    success_url = '/watchlist/' + str(request.user.id)
    return HttpResponseRedirect(success_url)

@login_required
def dashboard(request):
    if request.method == 'POST':
        print('okay')
    recommend = client.send(RecommendItemsToUser(request.user.id, 9))
    recommend = recommend["recomms"]
    print(recommend)
    list1 = []
    for i in range(0,len(recommend)):
        print(int(recommend[i]['id']))
        print(recommend[i])
        list1.append(TVseries.objects.get(id=int(recommend[i]['id'])))
    return render(request, './show/dashboard.html', {'recommend': list1})


@login_required
def addRating(request):
    tvseries = TVseries.objects.all()[0:30]
    print(tvseries)
    return render(request, './show/addRating.html', {'tvseries': tvseries})


@login_required
def watch_list_add(request,id):
    tvseries = TVseries.objects.get(id=id)
    user = request.user
    profile = UserProfile.objects.get(user=user)
    watchlist = Watchlist.objects.create(user=profile,series=tvseries,percent=0)
    success_url = '/dashboard/'
    return HttpResponseRedirect(success_url)


@login_required
def add_rate(request,id):
    if request.method=="GET":
        series = TVseries.objects.get(id=id)
        return render(request, './show/addrate.html', {'series':series})
    else:
        rating = request.POST.get('rating', '')
        tvseries = TVseries.objects.get(id=id)
        user = request.user
        profile = UserProfile.objects.get(user=user)
        series_rating = SeriesRating.objects.create(user=profile,series=tvseries,rating=rating)
        name = user.id
        series = tvseries.id
        rate = int(rating)
        rate = (rate-10)/10
        request = AddRating(name, series, rate ,cascade_create=True)
        client.send(request)
        success_url = '/dashboard/'
        return HttpResponseRedirect(success_url)
