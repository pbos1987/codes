import requests

# Replace YOUR_API_KEY with your actual API key
API_KEY = "YOUR_API_KEY"

# Set the Printify product ID
product_id = "12345"  # Replace with your actual Printify product ID

# Set the Etsy listing properties
listing_properties = {
    "title": "Custom Shirt",
    "description": "A custom shirt created with the Printify API",
    "price": "25.00",
    "quantity": 1,
    "materials": ["cotton"],
    "tags": ["custom", "shirt"],
    "shipping_template_id": 12345,  # Replace with your actual shipping template ID
    "shop_section_id": 12345,  # Replace with your actual shop section ID
    "printify_product_id": product_id,
    "who_made": "i_did",
    "when_made": "made_to_order",
    "recipient": "men"
}

# Make a request to the Etsy API to create the listing
response = requests.post(
    "https://openapi.etsy.com/v2/listings",
    headers={
        "Content-Type": "application/json",
        "Authorization": f"bearer {API_KEY}"
    },
    params={
        "associations": f"PrintifyProduct:{product_id}"
    },
    json=listing_properties
)

# Print the response
print("Response:")
print(response.json())
