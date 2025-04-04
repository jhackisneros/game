class Moviles:
    def __init__(self):
        self.android = {
            "Samsung": [
                {"modelo": "Galaxy S23", "precio": 799.99},
                {"modelo": "Galaxy A54", "precio": 349.99},
                {"modelo": "Galaxy Z Fold 5", "precio": 1799.99}
            ],
            "Xiaomi": [
                {"modelo": "Redmi Note 12", "precio": 199.99},
                {"modelo": "Xiaomi 13 Pro", "precio": 999.99},
                {"modelo": "Poco X5", "precio": 249.99}
            ],
            "OnePlus": [
                {"modelo": "OnePlus 11", "precio": 699.99},
                {"modelo": "OnePlus Nord CE 3", "precio": 329.99},
                {"modelo": "OnePlus 10T", "precio": 549.99}
            ]
        }
        self.apple = [
            {"modelo": "iPhone 14", "precio": 899.99},
            {"modelo": "iPhone 14 Pro", "precio": 1099.99},
            {"modelo": "iPhone SE (2022)", "precio": 429.99}
        ]

    def mostrar_opciones(self):
        print("\nTipos de Móviles:")
        print("1. Android")
        print("2. Apple")
        eleccion = input("Selecciona una opción (1-2): ").strip()

        if eleccion == "1":
            self.mostrar_android()
        elif eleccion == "2":
            self.mostrar_apple()
        else:
            print("Opción no válida. Intenta nuevamente.")

    def mostrar_android(self):
        print("\nMarcas de Android disponibles:")
        for idx, marca in enumerate(self.android.keys(), start=1):
            print(f"{idx}. {marca}")

        eleccion = input("Selecciona una marca (1-3): ").strip()
        marcas = list(self.android.keys())
        if eleccion.isdigit() and 1 <= int(eleccion) <= len(marcas):
            marca_seleccionada = marcas[int(eleccion) - 1]
            self.mostrar_modelos_android(marca_seleccionada)
        else:
            print("Opción no válida. Intenta nuevamente.")

    def mostrar_modelos_android(self, marca):
        print(f"\nModelos de {marca}:")
        modelos = self.android[marca]
        for idx, modelo in enumerate(modelos, start=1):
            print(f"{idx}. {modelo['modelo']} - ${modelo['precio']:.2f}")

        eleccion = input("Selecciona un modelo para comprar (1-3) o presiona Enter para salir: ").strip()
        if eleccion.isdigit() and 1 <= int(eleccion) <= len(modelos):
            self.comprar_movil(modelos[int(eleccion) - 1])
        elif eleccion == "":
            print("Regresando al menú principal.")
        else:
            print("Opción no válida. Intenta nuevamente.")

    def mostrar_apple(self):
        print("\nModelos de Apple disponibles:")
        for idx, modelo in enumerate(self.apple, start=1):
            print(f"{idx}. {modelo['modelo']} - ${modelo['precio']:.2f}")

        eleccion = input("Selecciona un modelo para comprar (1-3) o presiona Enter para salir: ").strip()
        if eleccion.isdigit() and 1 <= int(eleccion) <= len(self.apple):
            self.comprar_movil(self.apple[int(eleccion) - 1])
        elif eleccion == "":
            print("Regresando al menú principal.")
        else:
            print("Opción no válida. Intenta nuevamente.")

    def comprar_movil(self, modelo):
        print(f"\nHas seleccionado '{modelo['modelo']}' con un precio de ${modelo['precio']:.2f}.")
        confirmacion = input("¿Deseas comprar este móvil? (s/n): ").strip().lower()
        if confirmacion == "s":
            print(f"¡Gracias por tu compra! Disfruta de tu nuevo móvil '{modelo['modelo']}'.")
        else:
            print("Compra cancelada.")