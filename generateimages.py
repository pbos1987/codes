import requests

# Replace YOUR_API_KEY with your actual API key
API_KEY = "YOUR_API_KEY"

# Set the keyword for which you want to generate images
keyword = "dog"

# Set the number of images you want to generate
num_images = 10

# Set the image size (width and height in pixels)
image_size = 512

# Set the image format (jpeg or png)
image_format = "jpeg"

# Set the image style (0-2, with 0 being the most realistic and 2 being the most stylized)
image_style = 0

# Set the image encoding (base64 or binary)
image_encoding = "base64"

# Make a request to the DALL-E 2 API to generate images
response = requests.post(
    "https://api.openai.com/v1/images/generations",
    headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    },
    json={
        "model": "image-alpha-001",
        "prompt": f"{keyword} x{num_images}",
        "num_images": num_images,
        "size": f"{image_size}x{image_size}",
        "response_format": image_format,
        "style": image_style,
        "response_encoding": image_encoding
    }
)

# Parse the response and extract the generated images
images = response.json()["data"]

# Print the images
print("Generated images:")
for i, image in enumerate(images):
    print(f"Image {i+1}:")
    print(image)
