from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    photo = models.ImageField(upload_to='users', blank=True, null=True)
    gender = models.CharField(max_length=6, blank=True, null=True)
    interests = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.user)

class TVseries(models.Model):
    name = models.CharField(max_length = 100, default=None)

    def __str__(self):
        return self.name



class SeriesRating(models.Model):
	series = models.ForeignKey(TVseries, on_delete=models.CASCADE, related_name='series')
	user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='userprofile')
	rating = models.PositiveIntegerField(validators=[MaxValueValidator(10)], null=True, blank=True)
    
