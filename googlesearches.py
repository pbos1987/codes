import requests

# Replace YOUR_API_KEY with your actual API key
API_KEY = "YOUR_API_KEY"

# Make a request to the Google Trends API to get the top 10 trending searches
response = requests.get(f"https://trends.google.com/trends/api/v1/trendingsearches/daily?hl=en-US&tz=-120&key={API_KEY}")

# Parse the response and extract the top 10 trending searches
trending_searches = response.json()["trendingSearchesDays"][0]["trendingSearches"]
top_10_searches = [search["title"]["query"] for search in trending_searches[:10]]

# Print the top 10 trending searches
print("Top 10 trending searches:")
for i, search in enumerate(top_10_searches):
    print(f"{i+1}. {search}")
