import requests

# Set the Trakt API URL and your API key
trakt_url = 'https://api.trakt.tv'
trakt_api_key = 'YOUR_API_KEY'

# Set the Sonarr API URL and your API key
sonarr_url = 'http://localhost:8989/api'
sonarr_api_key = 'YOUR_API_KEY'

# Set the headers for the API requests
trakt_headers = {
    'Content-Type': 'application/json',
    'trakt-api-version': '2',
    'trakt-api-key': trakt_api_key
}
sonarr_headers = {'X-Api-Key': sonarr_api_key}

# Send a GET request to the Trakt API to get the top 5 trending TV shows
response = requests.get(f'{trakt_url}/shows/trending', headers=trakt_headers)

# Check the status code of the response
if response.status_code == 200:
    # If the request was successful, parse the response JSON
    trending_shows = response.json()

    # Loop through the TV shows and add them to Sonarr using their TVDB IDs
    for show in trending_shows[:5]:  # get the top 5 shows
        tvdb_id = show['show']['ids']['tvdb']  # get the TVDB ID of the show
        title = show['show']['title']  # get the title of the show

        # Set the parameters for the Sonarr API request
        params = {
            'tvdbId': tvdb_id,
            'qualityProfileId': 1,  # change this to the ID of the desired quality profile
            'title': title,
            'titleSlug': title.lower().replace(' ', '-'),
            'addOptions': {
                'ignoreEpisodesWithFiles': False,
                'ignoreEpisodesWithoutFiles': False
            }
        }

        # Send a POST request to the Sonarr API to add the TV show to the library
        response = requests.post(f'{sonarr_url}/series/lookup', json=params, headers=sonarr_headers)
        if response.status_code == 201:
            print(f'Successfully added {title} to Sonarr')
        else:
            print(f'Error adding {title} to Sonarr: {response.text}')
else:
    # If the request was not successful, print the error message
    print(f'Error getting trending TV shows: {response.text}')
