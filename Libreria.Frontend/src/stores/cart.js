import { defineStore } from "pinia";

export const useCartStore = defineStore("cart", {
  state: () => ({
    items: []
  }),
  actions: {
    addToCart(libro) {
      if (!libro.id) {
        console.error("El libro no tiene id:", libro);
        return;
      }

      const existing = this.items.find(i => i.id === libro.id);
      if (existing) {
        existing.cantidad += 1;
      } else {
        this.items.push({ ...libro, cantidad: 1 });
      }
    },
    removeFromCart(id) {
      this.items = this.items.filter(i => i.id !== id);
    },
    clearCart() {
      this.items = [];
    },
    toVentaPayload(clienteId) {
        return {
            cliente_id: clienteId,
            libros: this.items.map((i) => ({
            libro_id: i.id,
            cantidad: i.cantidad,
            })),
        };
    }
  },
    getters: {
    totalItems: (state) =>
      state.items.reduce((sum, item) => sum + item.cantidad, 0),
    totalPrice: (state) =>
      state.items.reduce((sum, item) => sum + item.precio * item.cantidad, 0),
  },
});
