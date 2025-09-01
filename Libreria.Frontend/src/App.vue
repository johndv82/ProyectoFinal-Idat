<script setup>
</script>

<template>

  <nav class="navbar is-info" role="navigation" aria-label="main navigation" >
    <div class="navbar-brand">
      <a class="navbar-item" href="/">
        <img class="logo" src="@/assets/logo.png"></img>
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
            <a class="button is-link">
              <strong>Sign up</strong>
            </a>
            <a class="button is-light">
              Log in
            </a>
          </div>
        </div>
      </div>
    </div>
  </nav>
  <main>
    <router-view />
  </main>
</template>

<style scoped>
.logo{
  display: block;
}
.navbar {
  position: sticky;
  top: 0;
  z-index: 30;
}
</style>
