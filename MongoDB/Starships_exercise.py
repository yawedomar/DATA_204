# Importing packages
import pymongo
import json 
import requests

# Using the Star wars database and Connecting
client = pymongo.MongoClient()
db = client['starships']
print(db)

# Retrieving the starship data
def starships_api_data():  
    starship_page = []
    response = requests.get("https://swapi.dev/api/starships")
    data = response.json()
    starship_page += data['results']
    while data['next'] is not None:   # gets all the data in all pages
        data = requests.get(data["next"]).json()
        starship_page += data['results']   # Adds startships information into starship_page
    return starship_page

# Utilising the Api function to retrieve additional data 
def starships_info():
    starship_data = []
    for starships in starships_api_data():
        starship_data.append(requests.get(starships).json()['result']['properties'])
    return starship_data


# Extracts the name of the pilot to find ID and replace the URL 
def get_pilot_id():
    pilot_name = []
    starship_data = starships_info()
    for pilot in starship_data:
        if pilot['pilot'] ==[]:
            pass
        else:
            pilot_id = []
            starship_pilots = pilot['pilots']
            for pilot in starship_pilots:
                pilot_n = requests.get(pilot).json()['result']['properties']['name']
                pilot_id = db.characters.find_one({"name":pilot}, {"_id":1})
                pilot_id.append(pilot_name)
            pilot['pilots'] = pilot_id
            pilot.update({'pilots':pilot_id})
        pilot_name.append(pilot)
    return pilot_name

# Drop the existing collection and create the  new starship collection
db.drop_collection("starships")
print('Dropped the Starship Collection')

db.create_collection("starships")
print('Created New Starship Collection')

all_startship_data = get_pilot_id()
for starship in all_startship_data:
    db.starships.insert_one(starship)

print("Starships info have been added successfully into the collection")

