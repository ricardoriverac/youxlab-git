import axios from "axios";

const dbFetch = axios.create({
  baseURL: "https://dragonball-api.com/api",
  headers: {
    "Content-Type": "application/json",
  },
});

export default dbFetch;
