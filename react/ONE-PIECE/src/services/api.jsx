import axios from "axios";

const api = axios.create({
  method: "GET",
  baseURL: "https://api.api-onepiece.com/v2/characters/en",
  headers: {
    "Content-Type": "application/json",
  },
});

export default api;
