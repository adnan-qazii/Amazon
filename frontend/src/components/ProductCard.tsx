type ProductProps = {
  id: number;
  name: string;
  price: number;
  image?: string;
};

export default function ProductCard({ name, price, image }: ProductProps) {
  return (
    <div style={{
      backgroundColor: "#fff",
      borderRadius: "16px",
      overflow: "hidden",
      boxShadow: "0 2px 8px rgba(0,0,0,0.08)",
      transition: "all 0.3s ease",
      cursor: "pointer",
      border: "2px solid transparent"
    }}
    onMouseEnter={e => {
      e.currentTarget.style.transform = "translateY(-8px)";
      e.currentTarget.style.boxShadow = "0 12px 24px rgba(0,0,0,0.15)";
      e.currentTarget.style.borderColor = "#3b82f6";
    }}
    onMouseLeave={e => {
      e.currentTarget.style.transform = "translateY(0)";
      e.currentTarget.style.boxShadow = "0 2px 8px rgba(0,0,0,0.08)";
      e.currentTarget.style.borderColor = "transparent";
    }}>
      {/* Image with Badge */}
      <div style={{
        position: "relative",
        width: "100%",
        height: "280px",
        backgroundColor: "#fafafa",
        overflow: "hidden"
      }}>
        <img
          src={image || "https://via.placeholder.com/500x500/3b82f6/ffffff?text=Product"}
          alt={name}
          style={{
            width: "100%",
            height: "100%",
            objectFit: "cover"
          }}
        />
        <div style={{
          position: "absolute",
          top: "15px",
          left: "15px",
          backgroundColor: "#10b981",
          color: "#fff",
          padding: "6px 14px",
          borderRadius: "20px",
          fontSize: "0.8rem",
          fontWeight: "700",
          textTransform: "uppercase",
          letterSpacing: "0.5px"
        }}>
          New
        </div>
      </div>

      {/* Content */}
      <div style={{
        padding: "20px"
      }}>
        {/* Rating Stars */}
        <div style={{
          marginBottom: "10px",
          color: "#f59e0b",
          fontSize: "0.9rem"
        }}>
          ⭐⭐⭐⭐⭐
        </div>

        <h3 style={{
          fontSize: "1.2rem",
          margin: "0 0 12px 0",
          color: "#1f2937",
          fontWeight: "700",
          lineHeight: "1.4"
        }}>
          {name}
        </h3>

        {/* Price and Button */}
        <div style={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          marginTop: "18px"
        }}>
          <div>
            <p style={{
              fontSize: "0.85rem",
              color: "#9ca3af",
              margin: "0 0 4px 0",
              textDecoration: "line-through"
            }}>
              ${(price * 1.4).toFixed(2)}
            </p>
            <p style={{
              fontSize: "1.8rem",
              fontWeight: "800",
              color: "#2563eb",
              margin: 0,
              lineHeight: "1"
            }}>
              ${price.toFixed(2)}
            </p>
          </div>

          <button style={{
            padding: "12px 24px",
            background: "linear-gradient(135deg, #3b82f6, #2563eb)",
            color: "#fff",
            border: "none",
            borderRadius: "25px",
            fontSize: "0.95rem",
            fontWeight: "700",
            cursor: "pointer",
            transition: "all 0.3s ease",
            boxShadow: "0 4px 12px rgba(59,130,246,0.3)",
            textShadow: "1px 1px 2px rgba(0,0,0,0.1)"
          }}
          onMouseEnter={e => {
            e.currentTarget.style.transform = "scale(1.05)";
            e.currentTarget.style.boxShadow = "0 6px 16px rgba(59,130,246,0.4)";
          }}
          onMouseLeave={e => {
            e.currentTarget.style.transform = "scale(1)";
            e.currentTarget.style.boxShadow = "0 4px 12px rgba(59,130,246,0.3)";
          }}>
            🛒 Buy Now
          </button>
        </div>
      </div>
    </div>
  );
}
