<script setup>
import { ref } from "vue";
import { useAuthStore } from "@/stores/auth";
import { computed } from "vue";

import LoginModal from "@/components/LoginModal.vue";
import RegisterModal from "@/components/RegisterModal.vue";

const auth = useAuthStore();
const isAuthenticated = computed(() => auth.isAuthenticated);
const username = computed(() => auth.username);

const showLogin = ref(false);
const showRegister = ref(false);
</script>

<template>
  <nav class="navbar is-info" role="navigation" aria-label="main navigation" >
    <div class="navbar-brand">
      <a class="navbar-item" href="/">
        <img class="logo" src="@/assets/logo.png" />
        New Book
      </a>
    </div>

    <div id="navbarBasicExample" class="navbar-menu">
      <div class="navbar-start">
        <router-link class="navbar-item" to="/">Inicio</router-link>
        <router-link class="navbar-item" to="/carrito">Carrito</router-link>
        <router-link class="navbar-item" to="/pedidos">Pedidos</router-link>
      </div>

      <div class="navbar-end">
        <div class="navbar-item">
          <div class="buttons">
            <template v-if="!isAuthenticated">
              <a class="button is-link" @click="showRegister = true">
                <strong>Sign up</strong>
              </a>
              <a class="button is-light" @click="showLogin = true">
                Log in
              </a>
            </template>

            <template v-else>
              <span class="navbar-item">Hola, {{ username }}</span>
              <a class="button is-light" @click="auth.logout">Cerrar sesión</a>
            </template>
          </div>
        </div>
      </div>
    </div>
  </nav>

  <main>
    <router-view />
  </main>

  <LoginModal v-if="showLogin" @close="showLogin = false" />
  <RegisterModal v-if="showRegister" @close="showRegister = false" />
</template>
