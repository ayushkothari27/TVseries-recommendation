import csv
import random
from .models import *
from recombee_api_client.api_client import RecombeeClient
from recombee_api_client.exceptions import APIException
from recombee_api_client.api_requests import *

client = RecombeeClient('tvseries', 'hw3cPcSNe1QHai4F3VFDcjDZh0GLWr4uMSxEOO60Ns6I314N8Fch4y4abXfvPFs7')

requests = []
list_of_ratings = SeriesRating.objects.all()
for i in range(0,len(list_of_ratings)):
    name = list_of_ratings[i].user.id
    series = list_of_ratings[i].series.id
    rate = list_of_ratings[i].rating
    rate = (rate-10)/10
    print(str(name) + ' ' + str(series) + ' ' + str(rate))
    request = AddRating(name, series, rate ,cascade_create=True)
    requests.append(request)

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
