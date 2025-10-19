import axios from "axios";

const BASE_URL = "http://localhost:5000"; // your Flask backend

export const loginUser = async (email: string, password: string) => {
  try {
    const response = await axios.post(`${BASE_URL}/login`, {
      email,
      password,
    });
    return response.data; // should return { token: "..." } from backend
  } catch (error: any) {
    console.error("Login error:", error);
    throw error.response?.data || { message: "Login failed" };
  }
};
