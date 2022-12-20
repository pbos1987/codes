import asyncio
import aiohttp

async def add_tv_series(title, release_year, overview):
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
    async with aiohttp.ClientSession() as session:
        async with session.post("http://localhost:8989/api/series", headers=headers, json=payload) as response:
            # Print the response status code to check if the TV series was added successfully
            print(response.status_code)

async def main():
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
    async with aiohttp.ClientSession() as session:
        async with session.get(base_url + "discover/tv", params=params) as response:
            # Check the status code of the response
            if response.status_code == 200:
                # Load the response data into a dictionary
                data = await response.json()

                # Iterate through the results and add each TV series to Sonarr
                tasks = []
                for result in data["results"]:
                    # Get the TV series details
                    title = result["name"]
                    release_year = result["first_air_date"][:4]
                    overview = result["overview"]

                    task = asyncio.create_task(add_tv_series(title, release_year, overview))
                    tasks.append(task)
                await asyncio.gather(*tasks)
            else:
                # Print the error message if the API call fails
                print(await response.text())

asyncio.run(main())
