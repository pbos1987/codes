import base64
import requests

# Replace YOUR_API_KEY with your actual API key
API_KEY = "YOUR_API_KEY"

# Read the PNG image file and encode it as base64
with open("image.png", "rb") as image_file:
    image_data = image_file.read()
    image_base64 = base64.b64encode(image_data).decode("utf-8")

# Set the shirt properties
shirt_properties = {
    "name": "Custom Shirt",
    "description": "A custom shirt created with the Printify API",
    "sku": "custom-shirt-001",
    "price": "25.00",
    "currency": "USD",
    "product_id": "4a8ab8ea-70a9-4816-9d9e-16b7f2f06fef",  # Unisex T-Shirt
    "external_id": "custom-shirt-001",
    "images": [
        {
            "type": "base64",
            "filename": "image.png",
            "content": image_base64
        }
    ]
}

# Make a request to the Printify API to create the shirt
response = requests.post(
    "https://api.printify.com/v1/products/custom.json",
    headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    },
    json=shirt_properties
)

# Print the response
print("Response:")
print(response.json())
