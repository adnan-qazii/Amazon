import axios from "axios";

const BASE_URL = "http://localhost:5000"; // Flask backend URL

export const registerUser = async (username: string, email: string, password: string) => {
  try {
    const response = await axios.post(`${BASE_URL}/register`, {
      username,
      email,
      password
    });
    return response.data;
  } catch (error: any) {
    console.error("Error registering user:", error);
    throw error.response?.data || { message: "Registration failed" };
  }
};
