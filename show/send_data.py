import csv
import random
from .models import *
from recombee_api_client.api_client import RecombeeClient
from recombee_api_client.exceptions import APIException
from recombee_api_client.api_requests import *

client = RecombeeClient('tvseries', 'IG1t5vSWYgpJvClpbJZUn29oqnCu6QnIHoJdm9u5dRLom47i0WrpWrNKcZ9om21x')

requests = []
list_of_ratings = SeriesRating.objects.all()
print(list_of_ratings)
print(len(list_of_ratings))
for i in range(0,len(list_of_ratings)):
    name = list_of_ratings[i].user.id
    series = list_of_ratings[i].series.id
    rate = list_of_ratings[i].rating
    rate = (rate-10)/10
    print(str(name) + ' ' + str(series) + ' ' + str(rate))
    request = AddRating(name, series, rate ,cascade_create=True)
    requests.append(request)

print(len(requests))
print(requests)
try:
    print('sending')
    client.send(Batch(requests))
    print('Send')
except APIException as e:
	print(e)
except ResponseException as e:
    print(e)
except ApiTimeoutException as e:
    print(e)
except Exception as e:
    print(e)
