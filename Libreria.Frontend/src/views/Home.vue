<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import { useCartStore } from "@/stores/cart";
import { useToast } from "@/composables/useToast";

const libros = ref([]);
const query = ref("");
const cart = useCartStore();
const { showToast } = useToast();

function agregar(libro) {
    cart.addToCart(libro);
    showToast(`"${libro.titulo}" agregado al carrito 🛒`, "is-success");
}

const fetchLibros = async () => {
  try {
    const response = await axios.get("http://localhost:8000/libros", {
      params: { q: query.value },
    });
    libros.value = response.data;
  } catch (error) {
    console.error("Error cargando libros", error);
  }
};

onMounted(() => {
  fetchLibros();
});
</script>

<template>
  <section class="section">
    <div class="container">
      <h1 class="title">Catálogo de Libros</h1>
      <div class="field has-addons">
        <div class="control has-icons-left is-expanded">
          <input
            v-model="query"
            class="input"
            type="text"
            placeholder="Buscar por título o autor"
          />
          <span class="icon is-small is-left">
            <i class="fas fa-search"></i>
          </span>
        </div>
        <div class="control">
          <button class="button is-info" @click="fetchLibros">
            Buscar
          </button>
        </div>
      </div>

      <div class="columns is-multiline">
        <div class="column is-one-quarter" v-for="libro in libros" :key="libro.id">
          <div class="card">
            <div class="card-image">
              <figure class="image is-2by3">
                <img :src="libro.portada" :alt="libro.titulo" />
              </figure>
            </div>

            <div class="card-content">
              <p class="title is-5">{{ libro.titulo }}</p>
              <p class="subtitle is-6">Autor: {{ libro.autor }}</p>
              <p class="is-size-7">ISBN: {{ libro.isbn }}</p>
              <p class="is-size-6 has-text-weight-semibold">
                S/. {{ libro.precio.toFixed(2) }}
              </p>
              <p class="is-size-7" v-if="libro.activo">
                Disponible desde: {{ new Date(libro.fecha_ingreso).toLocaleDateString() }}
              </p>
              <p class="is-size-7 has-text-danger" v-else>
                No disponible
              </p>
            </div>

            <footer class="card-footer">
              <button class="card-footer-item button is-small is-link" :disabled="!libro.activo" @click="agregar(libro)">
                Agregar al carrito
            </button>
            </footer>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
