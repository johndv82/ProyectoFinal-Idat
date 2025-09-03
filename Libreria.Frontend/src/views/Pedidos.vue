<script setup>
import { useAuthStore } from "@/stores/auth";
import { computed } from "vue";
import { ref, onMounted } from "vue";
import api from "@/api";

const auth = useAuthStore();

const pedidos = ref([]);
const loading = ref(true);
const error = ref(null);
const isAuthenticated = computed(() => auth.isAuthenticated);

async function cargarPedidos() {
  try {
    const res = await api.get(`/ventas/${auth.user_id}`
    );
    pedidos.value = Array.isArray(res.data) ? res.data : [];
  } catch (err) {
    error.value = err.response?.data?.detail || "Error cargando pedidos";
  } finally {
    loading.value = false;
  }
}

onMounted(() => {
    if(auth.isAuthenticated){
        cargarPedidos();
    }
});

</script>

<template>
    <div v-if="isAuthenticated">
        
    <section class="section">
        <div class="container">
        <h1 class="title">Mis Pedidos</h1>

        <div v-if="loading" class="notification is-info">Cargando pedidos...</div>
        <div v-else-if="error" class="notification is-danger">{{ error }}</div>
        <div v-else-if="!pedidos || pedidos.length === 0" class="notification is-warning">
            No tienes pedidos registrados.
        </div>
        <div v-else>
            <div
            v-for="pedido in pedidos"
            :key="pedido.id"
            class="box"
            >
            <h2 class="subtitle">
                Pedido #{{ pedido.id }} -
                {{ new Date(pedido.fecha).toLocaleString() }}
            </h2>

            <table class="table is-fullwidth is-striped is-hoverable">
                <thead>
                <tr>
                    <th>Título</th>
                    <th>Cantidad</th>
                    <th>Precio Unitario</th>
                    <th>Subtotal</th>
                </tr>
                </thead>
                <tbody>
                <tr v-for="libro in pedido.libros" :key="libro.libro_id">
                    <td>{{ libro.titulo }}</td>
                    <td>{{ libro.cantidad }}</td>
                    <td>S/ {{ libro.precio_unitario.toFixed(2) }}</td>
                    <td>S/ {{ (libro.precio_unitario * libro.cantidad).toFixed(2) }}</td>
                </tr>
                </tbody>
            </table>

            <p class="has-text-right has-text-weight-bold">
                Total: S/
                {{
                pedido.libros
                    .reduce((acc, l) => acc + l.precio_unitario * l.cantidad, 0)
                    .toFixed(2)
                }}
            </p>
            </div>
        </div>
        </div>
    </section>

    </div>
    <div v-else>
        Primero debe iniciar sesión para ver sus pedidos.
    </div>
</template>

<style scoped>

</style>
