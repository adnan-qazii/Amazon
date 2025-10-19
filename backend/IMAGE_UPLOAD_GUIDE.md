# Product Image Upload Guide

## Overview
Product images are now stored in the `uploads/products/` folder on your server. The `image` column in the database stores only the filename, not the full path.

## How It Works

### 1. **Storage Location**
- Images are saved to: `backend/uploads/products/`
- Each image gets a unique filename using UUID to prevent conflicts
- Allowed formats: PNG, JPG, JPEG, GIF, WEBP
- Max file size: 5MB

### 2. **Database Storage**
- The `image` column stores only the filename (e.g., `abc123-uuid_product.jpg`)
- NOT the full path or URL

### 3. **Accessing Images**
- Images are served via the route: `/products/images/<filename>`
- Full URL example: `http://localhost:5000/products/images/abc123-uuid_product.jpg`

## API Usage

### Create Product with Image

**Endpoint:** `POST /admin/products`

**Method 1: Using Form Data (with image file)**
```http
POST /admin/products
Content-Type: multipart/form-data
Authorization: Bearer <your-token>

Form fields:
- name: "Product Name"
- description: "Product Description"
- price: 29.99
- stock: 100
- image: <file>
```

**Example using Postman:**
1. Select POST request
2. Add Authorization header with Bearer token
3. Select "Body" → "form-data"
4. Add fields: name, description, price, stock
5. For image field, change type to "File" and upload your image

**Example using cURL:**
```bash
curl -X POST http://localhost:5000/admin/products \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -F "name=Laptop" \
  -F "description=Gaming laptop" \
  -F "price=999.99" \
  -F "stock=50" \
  -F "image=@/path/to/image.jpg"
```

**Method 2: Using JSON (without image)**
```http
POST /admin/products
Content-Type: application/json
Authorization: Bearer <your-token>

{
  "name": "Product Name",
  "description": "Product Description",
  "price": 29.99,
  "stock": 100
}
```

### Update Product with Image

**Endpoint:** `PUT /admin/products/<product_id>`

Same as create - supports both form-data (with image) and JSON (without image).

### Get Products

**Endpoint:** `GET /products`

**Response:**
```json
[
  {
    "id": 1,
    "name": "Laptop",
    "description": "Gaming laptop",
    "price": 999.99,
    "stock": 50,
    "image": "http://localhost:5000/products/images/abc123-uuid_laptop.jpg",
    "created_at": "2025-10-19T12:00:00",
    "updated_at": "2025-10-19T12:00:00"
  }
]
```

Note: The `image` field returns the full URL to access the image.

### Get Single Product

**Endpoint:** `GET /products/<product_id>`

Returns the same format as above.

## Frontend Integration

### Display Product Image
```javascript
// React/JavaScript example
const ProductCard = ({ product }) => {
  return (
    <div>
      <h3>{product.name}</h3>
      {product.image && (
        <img src={product.image} alt={product.name} />
      )}
      <p>${product.price}</p>
    </div>
  );
};
```

### Upload Product Image
```javascript
// React example
const uploadProduct = async (formData) => {
  const data = new FormData();
  data.append('name', formData.name);
  data.append('description', formData.description);
  data.append('price', formData.price);
  data.append('stock', formData.stock);
  data.append('image', formData.imageFile); // File object from input

  const response = await fetch('http://localhost:5000/admin/products', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${token}`
    },
    body: data
  });
  
  return await response.json();
};
```

### HTML Form Example
```html
<form id="productForm" enctype="multipart/form-data">
  <input type="text" name="name" placeholder="Product Name" required>
  <textarea name="description" placeholder="Description"></textarea>
  <input type="number" name="price" placeholder="Price" step="0.01" required>
  <input type="number" name="stock" placeholder="Stock" required>
  <input type="file" name="image" accept="image/*">
  <button type="submit">Create Product</button>
</form>
```

## Important Notes

1. **Image Deletion:** When you delete or update a product, the old image is automatically deleted from the filesystem
2. **Unique Filenames:** Images are saved with UUID prefixes to prevent filename conflicts
3. **Security:** Only admins can create/update products (protected by `@admin_required` decorator)
4. **File Validation:** Only allowed image formats are accepted
5. **No Image Required:** Products can be created without images (image field is nullable)

## Troubleshooting

### Images not uploading?
- Check that `uploads/products/` directory exists
- Verify file size is under 5MB
- Ensure file format is one of: PNG, JPG, JPEG, GIF, WEBP

### Images not displaying?
- Verify the image URL is accessible: `http://localhost:5000/products/images/<filename>`
- Check that the file exists in `uploads/products/` folder
- Ensure CORS is configured if accessing from a different domain

### Permission Issues?
- Make sure the `uploads/products/` directory has write permissions
- On Windows, check folder permissions in properties
