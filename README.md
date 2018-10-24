# TVseries-recommendation
This was a project for the course web technology in semester 5.

## Dataset
We are using this dataset to get a list of TV series.
https://www.kaggle.com/chasewillden/netflix-shows

## Recommendation:
We are using Recombee API for the recommendation system. 

## Scripts
- ```csv_reader.py``` : Reads the CSV file and add TV Series objects into the database and for demo purposes we created new user and rating objects in the same script.
- ```send_data.py``` : Sends the ratings objects to the Recombee API for initial demo purposes.

## Screenshots:
![screenshot from 2018-10-24 15-57-29](https://user-images.githubusercontent.com/29770201/47424661-c802c300-d7a5-11e8-93af-109b530a6ca7.png)
![screenshot from 2018-10-24 15-57-38](https://user-images.githubusercontent.com/29770201/47424663-c802c300-d7a5-11e8-81be-061f1f9e2f34.png)
![screenshot from 2018-10-24 15-57-49](https://user-images.githubusercontent.com/29770201/47424664-c802c300-d7a5-11e8-90bd-83109560b490.png)
![screenshot from 2018-10-24 15-58-09](https://user-images.githubusercontent.com/29770201/47424665-c89b5980-d7a5-11e8-8844-eb6b737ea563.png)
![screenshot from 2018-10-24 15-58-18](https://user-images.githubusercontent.com/29770201/47424666-c89b5980-d7a5-11e8-96d7-e705f4a76e4e.png)
![screenshot from 2018-10-24 15-58-41](https://user-images.githubusercontent.com/29770201/47424667-c89b5980-d7a5-11e8-80e2-95415344b9e3.png)


## TO DO:
- Google OAuth in login and register
- API that returns images when name of TV Series is passed( Currently it is hardcoded to FRIENDS)
- Edit button to change percentage on Watchlist page.
- Currently API only takes ratings but we would like to take genres and stuff as well.

## Contributors:
- [@purviljain](https://github.com/purviljain/)
- [@ParthJhunjhunwala](https://github.com/ParthJhunjhunwala/)
- [@aayushkothari11](https://github.com/aayushkothari11/)
