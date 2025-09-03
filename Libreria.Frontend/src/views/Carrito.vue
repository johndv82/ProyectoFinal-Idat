<script setup>
import { useCartStore } from "@/stores/cart";
import { useAuthStore } from "@/stores/auth";
import { ref, computed } from "vue";
import api from "@/api";

const cart = useCartStore();
const auth = useAuthStore();
const mensaje = ref("");
const user_id = computed(() => auth.user_id);
const isAuthenticated = computed(() => auth.isAuthenticated);

function increase(item) {
  if (item.cantidad < 3) {
    item.cantidad += 1;
  }
}

function decrease(item) {
  if (item.cantidad > 1) {
    item.cantidad -= 1;
  }
}

function removeItem(id) {
  cart.removeFromCart(id);
}

async function procesarCompra() {
  try {
    const payload = cart.toVentaPayload(user_id.value);
    const res = await api.post("/ventas/", payload);

    mensaje.value = `Compra registrada. ID: ${res.data.id}`;
    cart.clearCart();
  } catch (err) {
    mensaje.value = err.response?.data?.detail || "Error procesando compra";
  }
}
</script>

<template>
  <section class="section">
    <div class="container">
      <h1 class="title">Carrito de Compras</h1>

      <div v-if="cart.items.length === 0" class="notification is-info">
        Tu carrito está vacío.
      </div>

      <div v-else>
        <table class="table is-fullwidth is-striped is-hoverable">
          <thead>
            <tr>
              <th>Portada</th>
              <th>Título</th>
              <th>Autor</th>
              <th>Precio</th>
              <th>Cantidad</th>
              <th>Total</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in cart.items" :key="item.id">
              <td>
                <figure class="image is-2by3">
                  <img :src="item.portada" alt="Portada libro" />
                </figure>
              </td>
              <td>{{ item.titulo }}</td>
              <td>{{ item.autor }}</td>
              <td>S/ {{ item.precio.toFixed(2) }}</td>
              <td>
                <div class="field has-addons">
                  <p class="control">
                    <button class="button is-small" :disabled="item.cantidad == 1" @click="decrease(item)">-</button>
                  </p>
                  <p class="control">
                    <input
                      class="input is-small has-text-centered"
                      type="text"
                      :value="item.cantidad"
                      readonly
                      style="width: 40px"
                    />
                  </p>
                  <p class="control">
                    <button
                      class="button is-small"
                      @click="increase(item)"
                      :disabled="item.cantidad >= 3"
                    >
                      +
                    </button>
                  </p>
                </div>
              </td>
              <td>S/ {{ (item.precio * item.cantidad).toFixed(2) }}</td>
              <td>
                <button
                  class="button is-danger is-small"
                  @click="removeItem(item.id)"
                >
                  Eliminar
                </button>
              </td>
            </tr>
          </tbody>
        </table>

        <div class="box has-text-right">
          <p class="title is-5">
            Total: S/ {{ cart.totalPrice.toFixed(2) }}
          </p>
          <p class="subtitle is-6">
            {{ cart.totalItems }} artículo(s)
          </p>

          <div v-if="isAuthenticated">
            <button class="button is-primary mt-4" @click="procesarCompra" :disabled="cart.items.length === 0">
              Procesar Compra
            </button>
          </div>
          <div v-else>
             Primero debe iniciar sesión para procasar la compra.
          </div>


        </div>


      </div>

      <p v-if="mensaje" class="notification is-success mt-3">{{ mensaje }}</p>
    </div>
  </section>
</template>
