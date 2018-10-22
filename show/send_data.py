import csv
import random
from .models import *
from recombee_api_client.api_client import RecombeeClient
from recombee_api_client.exceptions import APIException
from recombee_api_client.api_requests import *

client = RecombeeClient('tvseries', 'Xfp4Upkxyb4DpUC99e2wjU3REiOwcbibJnCYqFq97Pt8uAZhwi2aVD1SPzzgEofM')

requests = []
list_of_ratings = SeriesRating.objects.all()
print(list_of_ratings)
print(len(list_of_ratings))
for i in range(0,len(list_of_ratings)):
    name = str(list_of_ratings[i].user)
    series = str(list_of_ratings[i].series)
    rate = int(list_of_ratings[i].rating)

    request = AddRating(name, series, rate ,cascade_create=True)
    requests.append(request)

print(len(requests))
print(requests)
try:
	client.send(Batch(requests))
except APIException as e:
	print(e)
except ResponseException as e:
    print(e)
except ApiTimeoutException as e:
    print(e)
except Exception as e:
    print(e)
