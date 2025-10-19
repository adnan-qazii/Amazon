import { useState, useEffect } from "react";
import ProductCard from "../components/ProductCard";
import { fetchProducts } from "../api/productApi";

type Product = {
  id: number;
  name: string;
  price: number;
  image?: string;
};

export default function Home() {
  const [products, setProducts] = useState<Product[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const getProducts = async () => {
      try {
        const data = await fetchProducts();
        setProducts(data);
      } catch (err) {
        console.error("Failed to fetch products:", err);
        setError("Failed to load products. Please make sure the backend is running.");
      } finally {
        setLoading(false);
      }
    };

    getProducts();
  }, []);

  if (loading) {
    return (
      <div style={{
        padding: "60px 20px",
        textAlign: "center",
        backgroundColor: "#f5f5f5",
        minHeight: "80vh"
      }}>
        <p style={{ fontSize: "1.2rem", color: "#666" }}>Loading products...</p>
      </div>
    );
  }

  if (error) {
    return (
      <div style={{
        padding: "60px 20px",
        textAlign: "center",
        backgroundColor: "#f5f5f5",
        minHeight: "80vh"
      }}>
        <p style={{ fontSize: "1.2rem", color: "#d32f2f", marginBottom: "20px" }}>
          {error}
        </p>
        <button
          onClick={() => window.location.reload()}
          style={{
            padding: "12px 30px",
            backgroundColor: "#667eea",
            color: "white",
            border: "none",
            borderRadius: "6px",
            fontSize: "1rem",
            cursor: "pointer"
          }}
        >
          Retry
        </button>
      </div>
    );
  }

  return (
    <div style={{
      backgroundColor: "#ffffff",
      minHeight: "100vh"
    }}>
      {/* Hero Banner */}
      <div style={{
        background: "linear-gradient(90deg, #1e3a8a 0%, #3b82f6 100%)",
        padding: "50px 20px",
        marginBottom: "40px"
      }}>
        <div style={{
          maxWidth: "1400px",
          margin: "0 auto",
          textAlign: "center"
        }}>
          <h1 style={{
            fontSize: "3rem",
            color: "#fff",
            marginBottom: "15px",
            fontWeight: "800",
            textShadow: "2px 2px 4px rgba(0,0,0,0.2)"
          }}>
            ✨ Trending Products
          </h1>
          <p style={{
            fontSize: "1.2rem",
            color: "#fff",
            marginBottom: "20px",
            opacity: 0.95
          }}>
            Shop the latest and greatest products
          </p>
          <div style={{
            display: "inline-block",
            backgroundColor: "rgba(255,255,255,0.3)",
            padding: "8px 20px",
            borderRadius: "20px",
            color: "#fff",
            fontWeight: "600"
          }}>
            📦 {products.length} Products in Stock
          </div>
        </div>
      </div>

      {/* Product Grid Section */}
      <div style={{
        maxWidth: "1400px",
        margin: "0 auto",
        padding: "0 20px 120px"
      }}>
        <div style={{
          display: "grid",
          gridTemplateColumns: "repeat(auto-fill, minmax(300px, 1fr))",
          gap: "30px"
        }}>
          {products.map(product => (
            <ProductCard
              key={product.id}
              id={product.id}
              name={product.name}
              price={product.price}
              image={product.image}
            />
          ))}
        </div>
      </div>
    </div>
  );
}
