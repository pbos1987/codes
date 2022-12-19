import requests
import json

# Emby API Key and headers
api_key = "YOUR_EMBY_API_KEY"
headers = {
    "Content-Type": "application/json",
    "X-MediaBrowser-Token": api_key
}

# Emby base URL
emby_url = "http://localhost:8096/emby"

# URL for Emby's create collection endpoint
create_collection_url = emby_url + "/Collections"

# Create the collection
collection_data = {
    "Name": "Trending Movies"
}
response = requests.post(create_collection_url, headers=headers, json=collection_data)

# Check the status code of the response
if response.status_code != 201:
    print("Failed to create collection. Status code:", response.status_code)
    exit()

# Parse the response as JSON
collection = response.json()

# Get the ID of the newly created collection
collection_id = collection["Id"]

# IMDB API Key and headers
imdb_api_key = "YOUR_IMDB_API_KEY"
imdb_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + imdb_api_key
}

# URL for IMDB's trending movies endpoint
trending_url = "https://api.imdb.com/Movies/trending"

# Send a GET request to the trending movies endpoint
response = requests.get(trending_url, headers=imdb_headers)

# Check the status code of the response
if response.status_code != 200:
    print("Failed to retrieve trending movies. Status code:", response.status_code)
    exit()

# Parse the response as JSON
trending_movies = response.json()

# Get the top 10 trending movies
top_trending_movies = trending_movies[:10]

# Print the titles of the top 10 trending movies
for movie in top_trending_movies:
    print(movie["title"])

# URL for Emby's add items to collection endpoint
add_to_collection_url = emby_url + "/Collections/" + collection_id + "/Items"

# Iterate over the top 10 trending movies and add them to the collection
for movie in top_trending_movies:
    # Construct the movie data to send to Emby
    movie_data = {
        "Name": movie["title"],
        "ProviderIds": {
            "Imdb": movie["imdbId"]
        }
    }
    # Send a POST request to the add items to collection endpoint
    response = requests.post(add_to_collection_url, headers=headers, json=movie_data)
    # Check the status code of the response
    if response.status_code != 201:
        print("Failed to add movie to collection. Status code:", response.status_code)
    else:
        print("Successfully added movie to collection:", movie["title"])
