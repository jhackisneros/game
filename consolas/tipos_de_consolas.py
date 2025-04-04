class Consolas:
    def __init__(self):
        self.xbox = [
            {"modelo": "Xbox Series X", "precio": 499.99},
            {"modelo": "Xbox Series S", "precio": 299.99},
            {"modelo": "Xbox One X", "precio": 399.99}
        ]
        self.playstation = [
            {"modelo": "PlayStation 5", "precio": 499.99},
            {"modelo": "PlayStation 4 Pro", "precio": 399.99},
            {"modelo": "PlayStation 4 Slim", "precio": 299.99}
        ]

    def mostrar_opciones(self):
        print("\nTipos de Consolas:")
        print("1. Xbox")
        print("2. PlayStation")
        eleccion = input("Selecciona una opción (1-2): ").strip()

        if eleccion == "1":
            self.mostrar_consolas(self.xbox, "Xbox")
        elif eleccion == "2":
            self.mostrar_consolas(self.playstation, "PlayStation")
        else:
            print("Opción no válida. Intenta nuevamente.")

    def mostrar_consolas(self, consolas, categoria):
        print(f"\nConsolas de {categoria}:")
        for idx, consola in enumerate(consolas, start=1):
            print(f"{idx}. {consola['modelo']} - ${consola['precio']:.2f}")

        eleccion = input("Selecciona una consola para comprar (1-3) o presiona Enter para salir: ").strip()
        if eleccion.isdigit() and 1 <= int(eleccion) <= len(consolas):
            self.comprar_consola(consolas[int(eleccion) - 1])
        elif eleccion == "":
            print("Regresando al menú principal.")
        else:
            print("Opción no válida. Intenta nuevamente.")

    def comprar_consola(self, consola):
        print(f"\nHas seleccionado '{consola['modelo']}' con un precio de ${consola['precio']:.2f}.")
        confirmacion = input("¿Deseas comprar esta consola? (s/n): ").strip().lower()
        if confirmacion == "s":
            print(f"¡Gracias por tu compra! Disfruta de tu nueva consola '{consola['modelo']}'.")
        else:
            print("Compra cancelada.")