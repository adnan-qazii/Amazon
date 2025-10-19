"""
Example: How to Test Product Image Upload

This file shows example requests for testing the image upload functionality.
"""

# Example 1: Create product with image using Python requests
"""
import requests

url = "http://localhost:5000/admin/products"
headers = {
    "Authorization": "Bearer YOUR_TOKEN_HERE"
}

# Prepare form data
data = {
    'name': 'Gaming Laptop',
    'description': 'High-performance gaming laptop with RTX 4090',
    'price': '1999.99',
    'stock': '25'
}

# Upload image file
files = {
    'image': open('laptop.jpg', 'rb')
}

response = requests.post(url, headers=headers, data=data, files=files)
print(response.json())
"""

# Example 2: Create product without image
"""
import requests

url = "http://localhost:5000/admin/products"
headers = {
    "Authorization": "Bearer YOUR_TOKEN_HERE",
    "Content-Type": "application/json"
}

data = {
    "name": "Wireless Mouse",
    "description": "Ergonomic wireless mouse",
    "price": 29.99,
    "stock": 100
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
"""

# Example 3: Get all products (with image URLs)
"""
import requests

url = "http://localhost:5000/products"
response = requests.get(url)
products = response.json()

for product in products:
    print(f"Product: {product['name']}")
    print(f"Image URL: {product['image']}")
    print(f"Price: ${product['price']}")
    print("---")
"""

# Example 4: Update product with new image
"""
import requests

product_id = 1
url = f"http://localhost:5000/admin/products/{product_id}"
headers = {
    "Authorization": "Bearer YOUR_TOKEN_HERE"
}

data = {
    'name': 'Updated Gaming Laptop',
    'price': '1899.99'
}

files = {
    'image': open('new_laptop_image.jpg', 'rb')
}

response = requests.put(url, headers=headers, data=data, files=files)
print(response.json())
"""

print("See IMAGE_UPLOAD_GUIDE.md for complete documentation")
