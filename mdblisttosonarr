import requests
import json

# Set the base URL for the MDBList API
base_url = "https://mdblist.com/api/"

# Set the API key for the MDBList API
api_key = "YOUR_API_KEY"

# Set the list ID
list_id = 12345

# Set the parameters for the API call
params = {
    "api_key": api_key,
    "language": "en-US"
}

# Make the API call to retrieve the list with the given ID
response = requests.get(base_url + "list/" + str(list_id), params=params)

# Check the status code of the response
if response.status_code == 200:
    # Load the response data into a dictionary
    data = response.json()

    # Iterate through the items in the list and add each entry to Sonarr
    for item in data["items"]:
        # Get the entry details
        title = item["name"]
        release_year = item["first_air_date"][:4]
        overview = item["overview"]

        # Add the entry to Sonarr
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
        
        # Print the response status code to check if the entry was added successfully
        print(response.status_code)

else:
    # Print the error message if the API call fails
    print(response.text)
