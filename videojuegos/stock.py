class Videojuegos:
    def __init__(self):
        self.categorias = {
            "1": {"nombre": "Terror", "juegos": [
                {"nombre": "Resident Evil", "precio": 59.99},
                {"nombre": "Silent Hill", "precio": 49.99},
                {"nombre": "Outlast", "precio": 19.99}
            ]},
            "2": {"nombre": "Lucha", "juegos": [
                {"nombre": "Street Fighter", "precio": 39.99},
                {"nombre": "Tekken", "precio": 44.99},
                {"nombre": "Mortal Kombat", "precio": 54.99}
            ]},
            "3": {"nombre": "Aventura", "juegos": [
                {"nombre": "The Legend of Zelda", "precio": 69.99},
                {"nombre": "Uncharted", "precio": 29.99},
                {"nombre": "Tomb Raider", "precio": 24.99}
            ]},
            "4": {"nombre": "Carreras", "juegos": [
                {"nombre": "Need for Speed", "precio": 34.99},
                {"nombre": "Forza Horizon", "precio": 59.99},
                {"nombre": "Gran Turismo", "precio": 49.99}
            ]},
        }

    def mostrar_categorias(self):
        print("\nCategorías de Videojuegos:")
        for key, value in self.categorias.items():
            print(f"{key}. {value['nombre']}")

        eleccion = input("Selecciona una categoría (1-4): ").strip()
        if eleccion in self.categorias:
            self.mostrar_juegos(eleccion)
        else:
            print("Opción no válida. Intenta nuevamente.")

    def mostrar_juegos(self, categoria_id):
        categoria = self.categorias[categoria_id]
        print(f"\nJuegos de {categoria['nombre']}:")
        for idx, juego in enumerate(categoria["juegos"], start=1):
            print(f"{idx}. {juego['nombre']} - ${juego['precio']:.2f}")

        eleccion = input("\nSelecciona un juego para comprar (1-3) o presiona Enter para salir: ").strip()
        if eleccion.isdigit() and 1 <= int(eleccion) <= len(categoria["juegos"]):
            self.comprar_juego(categoria["juegos"][int(eleccion) - 1])
        elif eleccion == "":
            print("Regresando al menú principal.")
        else:
            print("Opción no válida. Intenta nuevamente.")

    def comprar_juego(self, juego):
        print(f"\nHas seleccionado '{juego['nombre']}' con un precio de ${juego['precio']:.2f}.")
        confirmacion = input("¿Deseas comprar este juego? (s/n): ").strip().lower()
        if confirmacion == "s":
            print(f"¡Gracias por tu compra! Disfruta de '{juego['nombre']}'.")
        else:
            print("Compra cancelada.")