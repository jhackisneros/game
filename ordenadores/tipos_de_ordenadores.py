class Ordenadores:
    def __init__(self):
        self.nvidia = [
            {"modelo": "NVIDIA Shield TV Pro", "precio": 199.99},
            {"modelo": "Steam Deck (NVIDIA)", "precio": 399.99},
            {"modelo": "Alienware Alpha R2", "precio": 599.99}
        ]
        self.amd = [
            {"modelo": "PlayStation 5", "precio": 499.99},
            {"modelo": "Xbox Series X", "precio": 499.99},
            {"modelo": "Steam Deck (AMD)", "precio": 399.99}
        ]

    def mostrar_opciones(self):
        print("\nTipos de Consolas:")
        print("1. Consolas con gráfica NVIDIA")
        print("2. Consolas con gráfica AMD")
        eleccion = input("Selecciona una opción (1-2): ").strip()

        if eleccion == "1":
            self.mostrar_consolas(self.nvidia, "NVIDIA")
        elif eleccion == "2":
            self.mostrar_consolas(self.amd, "AMD")
        else:
            print("Opción no válida. Intenta nuevamente.")

    def mostrar_consolas(self, consolas, tipo_grafica):
        print(f"\nConsolas con gráfica {tipo_grafica}:")
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