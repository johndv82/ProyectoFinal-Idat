<script setup>
import { ref } from "vue";
import { useAuthStore } from "@/stores/auth";

const emit = defineEmits(["close"]);

const username = ref("");
const password = ref("");
const auth = useAuthStore();

const handleLogin = async () => {
  await auth.login(username.value, password.value);
  if (auth.isAuthenticated) {
    emit("close");
  }
};
</script>

<template>
  <div class="modal is-active">
    <div class="modal-background" @click="emit('close')"></div>
    <div class="modal-card">
      <header class="modal-card-head">
        <p class="modal-card-title">Iniciar sesión</p>
        <button class="delete" aria-label="close" @click="emit('close')"></button>
      </header>
      <section class="modal-card-body">
        <div class="field">
          <label class="label">Usuario</label>
          <input class="input" v-model="username" type="text" required placeholder="Username">
        </div>
        <div class="field">
          <label class="label">Contraseña</label>
          <input class="input" v-model="password" type="password" required placeholder="Password">
        </div>
        <p v-if="auth.error" class="has-text-danger">{{ auth.error }}</p>
      </section>
      <footer class="modal-card-foot">
        <button class="button is-primary" @click="handleLogin">Ingresar</button>
        <button class="button" @click="emit('close')">Cancelar</button>
      </footer>
    </div>
  </div>
</template>
