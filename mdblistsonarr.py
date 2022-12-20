import requests
import json

# Set the base URL for the MDBList API
base_url = "https://mdblist.com/api/"

# Set the API key for the MDBList API
api_key = "YOUR_API_KEY"

# Set the parameters for the API call
params = {
    "api_key": api_key,
    "type": "series",
    "sort_by": "popularity.desc"
}

# Make the API call to retrieve the list of TV series
response = requests.get(base_url + "discover/tv", params=params)

# Check the status code of the response
if response.status_code == 200:
    # Load the response data into a dictionary
    data = response.json()

    # Iterate through the results and add each TV series to Sonarr
    for result in data["results"]:
        # Get the TV series details
        title = result["name"]
        release_year = result["first_air_date"][:4]
        overview = result["overview"]

        # Add the TV series to Sonarr
        # Replace the placeholder values with your Sonarr API information
        headers = {
            "X-Api-Key": "YOUR_SONARR_API_KEY"
        }
        payload = {
            "title": title,
            "year": release_year,
            "qualityProfileId": 1,
            "titleSlug": title.lower().replace(" ", "-"),
            "images": [],
            "seasons": [
                {
                    "seasonNumber": 1,
                    "monitored": True
                }
            ],
            "rootFolderPath": "YOUR_ROOT_FOLDER_PATH",
            "addOptions": {
                "ignoreEpisodesWithFiles": True,
                "ignoreEpisodesWithoutFiles": True
            }
        }
        response = requests.post("http://localhost:8989/api/series", headers=headers, json=payload)
        
        # Print the response status code to check if the TV series was added successfully
        print(response.status_code)

else:
    # Print the error message if the API call fails
    print(response.text)
