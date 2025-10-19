import { useEffect, useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

interface UserProfile {
  id: number;
  username: string;
  email: string;
  created_at: string;
}

export default function Profile() {
  const [user, setUser] = useState<UserProfile | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchProfile = async () => {
      const token = localStorage.getItem("token");
      if (!token) {
        navigate("/login"); // redirect if not logged in
        return;
      }

      try {
        const response = await axios.get("http://localhost:5000/profile", {
          headers: {
            Authorization: `Bearer ${token}`, // send token in header
          },
        });
        setUser(response.data);
      } catch (err: any) {
        console.error(err);
        setError("Failed to fetch profile. Please login again.");
        localStorage.removeItem("token");
        navigate("/login");
      } finally {
        setLoading(false);
      }
    };

    fetchProfile();
  }, [navigate]);

  if (loading) return (
    <div style={{
      minHeight: "100vh",
      background: "linear-gradient(90deg, #1e3a8a 0%, #3b82f6 100%)",
      display: "flex",
      justifyContent: "center",
      alignItems: "center"
    }}>
      <p style={{ color: "#fff", fontSize: "1.3rem" }}>Loading...</p>
    </div>
  );

  if (error) return (
    <div style={{
      minHeight: "100vh",
      background: "linear-gradient(90deg, #1e3a8a 0%, #3b82f6 100%)",
      display: "flex",
      justifyContent: "center",
      alignItems: "center"
    }}>
      <p style={{ color: "#ef4444", fontSize: "1.3rem", background: "#fff", padding: 24, borderRadius: 12 }}>{error}</p>
    </div>
  );

  return (
    <div style={{
      minHeight: "100vh",
      background: "linear-gradient(90deg, #1e3a8a 0%, #3b82f6 100%)",
      display: "flex",
      justifyContent: "center",
      alignItems: "center",
      padding: "120px 20px"
    }}>
      <div style={{
        background: "#fff",
        borderRadius: "18px",
        boxShadow: "0 8px 30px rgba(0,0,0,0.15)",
        padding: "48px 36px 36px 36px",
        maxWidth: "420px",
        width: "100%",
        textAlign: "center"
      }}>
        <div style={{
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          marginBottom: "24px"
        }}>
          <div style={{
            width: 90,
            height: 90,
            borderRadius: "50%",
            background: "linear-gradient(135deg, #3b82f6 60%, #1e3a8a 100%)",
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            marginBottom: 18
          }}>
            <span style={{ fontSize: 48, color: "#fff" }}>👤</span>
          </div>
          <h1 style={{ fontSize: "2rem", color: "#1e3a8a", fontWeight: 800, margin: 0 }}>Your Profile</h1>
        </div>
        {user && (
          <div style={{ textAlign: "left", lineHeight: "2.1rem", fontSize: "1.08rem", color: "#1e293b" }}>
            <p><strong>ID:</strong> {user.id}</p>
            <p><strong>Username:</strong> {user.username}</p>
            <p><strong>Email:</strong> {user.email}</p>
            <p><strong>Joined:</strong> {new Date(user.created_at).toLocaleDateString()}</p>
          </div>
        )}
      </div>
    </div>
  );
}
