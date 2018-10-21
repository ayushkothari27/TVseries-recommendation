from django.conf.urls import url
from . import views

app_name = 'show'
urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/(\d+)/$', views.profile, name='profile'),
]
