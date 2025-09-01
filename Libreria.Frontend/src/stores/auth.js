import { defineStore } from "pinia";
import axios from "axios";

export const useAuthStore = defineStore("auth", {
  state: () => ({
    isAuthenticated: localStorage.getItem("isAuthenticated") === "true",
    username: localStorage.getItem("username") || null,
    error: null,
  }),
  actions: {
    async login(username, password) {
      try {
        await axios.post(
          "http://localhost:8000/auth/login",
          {},
          {
            auth: { username, password },
          }
        );

        this.isAuthenticated = true;
        this.username = username;
        this.error = null;

        // guardar en localStorage
        localStorage.setItem("isAuthenticated", "true");
        localStorage.setItem("username", username);
      } catch (err) {
        this.isAuthenticated = false;
        this.username = null;
        this.error = err.response?.data?.detail || "Error de autenticación";

        // limpiar localstorage
        localStorage.removeItem("isAuthenticated");
        localStorage.removeItem("username");
      }
    },

    async register(username, email, password) {
      try {
        await axios.post("http://localhost:8000/auth/register", {
          username,
          email,
          password,
        });

        await this.login(username, password);
      } catch (err) {
        this.error = err.response?.data?.detail || "Error en el registro";
      }
    },

    logout() {
      this.isAuthenticated = false;
      this.username = null;
      this.error = null;

      localStorage.removeItem("isAuthenticated");
      localStorage.removeItem("username");
    },
  },
});
