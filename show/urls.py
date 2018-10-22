from django.conf.urls import url
from . import views
from django.views import View
from show.views import *

app_name = 'show'
urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/(\d+)/$', views.profile, name='profile'),
    url(r'^watchlist/(\d+)/$', views.watchlist, name='watchlist'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^addRating/$', views.addRating, name='addRating'),
    url(r'^watchlist-delete/(?P<pk>[0-9]+)/$', WatchlistDeleteView.as_view(), name='watchlist_delete'),
    url(r'^watchlist-complete/(\d+)/$', views.WatchlistCompView, name='watchlist_comp'),
    url(r'^watchlist-add/(\d+)/$', views.watch_list_add, name='watch_list_add'),
    url(r'^add_rate/(\d+)/$', views.add_rate, name='add_rate'),
]
