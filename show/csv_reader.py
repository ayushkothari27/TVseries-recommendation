import csv
import random
from .models import *


with open("/home/aayush/Desktop/WD-project/csv/Netflix_Shows.csv", encoding='latin-1') as f:
    reader = list(csv.reader(f, delimiter=','))[1:]
    for row in reader:
        name = row[0]
        usernames = ['messi','suarez','coutinho','neymar','villa','iniesta','xavi','busquests','dembele','ronaldo','hazard','pepe','robert']
        series, created = TVseries.objects.get_or_create(name=name)
        series.save()
        xyz = random.randint(0,len(usernames)-1)
        user, created = User.objects.get_or_create(username=usernames[xyz])
        if created:
            user.set_password('pass@123')
            user.first_name = random.choice(['Leo', 'Luis', 'Phillipe', 'Ousmane','Andres'])
            user.last_name = random.choice(['Messi', 'Suarez', 'Neymar','Kothari'])
            user.save()
            profile = UserProfile(user=user)
            profile.save()
        else:
            profile = UserProfile.objects.get(user=user)
        ratings, created = SeriesRating.objects.get_or_create(user=profile, series=series)
        if created:
            ratings.rating = random.randint(1,10)
            ratings.save()
        else:
            pass
