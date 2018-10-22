from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(TVseries)
admin.site.register(SeriesRating)
admin.site.register(Watchlist)
