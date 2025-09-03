<script setup>
import { ref, onMounted } from "vue";
import api from "@/api";

const libros = ref([]);

const showModal = ref(false);
const form = ref({
  id: null,
  titulo: "",
  isbn: "",
  autor: "",
  precio: 0,
  portada: "",
  activo: true
});

const message = ref("");
const messageType = ref("is-success");

// Cargar libros
async function cargarLibros() {
  try {
    const res = await api.get("/libros/");
    libros.value = res.data;
  } catch (err) {
    console.error(err);
  }
}

function nuevoLibro() {
  form.value = { id: null, titulo: "", isbn: "", autor: "", precio: 0, portada: "", activo: true };
  showModal.value = true;
}

function editarLibro(libro) {
  form.value = { ...libro };
  showModal.value = true;
}

// Guardar libro
async function guardarLibro() {
  try {
    if (form.value.id) {
      await api.put(`/libros/${form.value.id}`, form.value);
      message.value = "Libro actualizado correctamente";
    } else {
      await api.post("/libros/", form.value);
      message.value = "Libro creado correctamente";
    }
    showModal.value = false;
    await cargarLibros();
    setTimeout(() => (message.value = ""), 3000);
  } catch (err) {
    console.error(err);
    message.value = "Error al guardar el libro";
    messageType.value = "is-danger";
    setTimeout(() => (message.value = ""), 3000);
  }
}

async function eliminarLibro(id) {
  if (!confirm("¿Estás seguro de eliminar este libro?")) return;
  try {
    await api.delete(`/libros/${id}`);
    message.value = "Libro eliminado correctamente";
    await cargarLibros();
    setTimeout(() => (message.value = ""), 3000);
  } catch (err) {
    console.error(err);
    message.value = "Error al eliminar el libro";
    messageType.value = "is-danger";
    setTimeout(() => (message.value = ""), 3000);
  }
}


onMounted(() => {
  cargarLibros();
});
</script>

<template>
  <section class="section">
    <div class="container">
      <h1 class="title">Mantenimiento de Libros</h1>

      <div v-if="message" class="notification" :class="messageType">{{ message }}</div>

      <button class="button is-primary mb-4" @click="nuevoLibro">Nuevo Libro</button>

      <table class="table is-fullwidth is-striped is-hoverable">
        <thead>
          <tr>
            <th>ID</th>
            <th>Título</th>
            <th>ISBN</th>
            <th>Autor</th>
            <th>Precio</th>
            <th>Portada</th>
            <th>Activo</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="libro in libros" :key="libro.id">
            <td>{{ libro.id }}</td>
            <td>{{ libro.titulo }}</td>
            <td>{{ libro.isbn }}</td>
            <td>{{ libro.autor }}</td>
            <td>S/ {{ libro.precio.toFixed(2) }}</td>
            <td>{{ libro.portada }}</td>
            <td>{{ libro.activo ? "Sí" : "No" }}</td>
            <td>
              <button class="button is-small is-info mr-1" @click="editarLibro(libro)">Editar</button>
              <button class="button is-small is-danger" @click="eliminarLibro(libro.id)">Eliminar</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Modal de formulario -->
    <div class="modal" :class="{ 'is-active': showModal }">
      <div class="modal-background" @click="showModal = false"></div>
      <div class="modal-card">
        <header class="modal-card-head">
          <p class="modal-card-title">{{ form.id ? "Editar Libro" : "Nuevo Libro" }}</p>
          <button class="delete" aria-label="close" @click="showModal = false"></button>
        </header>
        <section class="modal-card-body">
          <div class="field">
            <label class="label">Título</label>
            <div class="control">
              <input v-model="form.titulo" class="input" type="text" />
            </div>
          </div>
          <div class="field">
            <label class="label">ISBN</label>
            <div class="control">
              <input v-model="form.isbn" class="input" type="text" />
            </div>
          </div>
          <div class="field">
            <label class="label">Autor</label>
            <div class="control">
              <input v-model="form.autor" class="input" type="text" />
            </div>
          </div>
          <div class="field">
            <label class="label">Precio</label>
            <div class="control">
              <input v-model.number="form.precio" class="input" type="number" step="0.01" />
            </div>
          </div>
          <div class="field">
            <label class="label">Portada URL</label>
            <div class="control">
              <input v-model="form.portada" class="input" type="text" />
            </div>
          </div>
          <div class="field">
            <label class="checkbox">
              <input type="checkbox" v-model="form.activo" />
              Activo
            </label>
          </div>
        </section>
        <footer class="modal-card-foot">
          <button class="button is-success" @click="guardarLibro">Guardar</button>
          <button class="button" @click="showModal = false">Cancelar</button>
        </footer>
      </div>
    </div>
  </section>
</template>

<style scoped>
</style>
