import axios from "axios";

const BASE_URL = "http://localhost:5000"; // Flask backend URL

export const fetchProducts = async () => {
  try {
    const response = await axios.get(`${BASE_URL}/products`);
    return response.data;
  } catch (error) {
    console.error("Error fetching products:", error);
    throw error;
  }
};
