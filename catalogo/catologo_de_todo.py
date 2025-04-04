from videojuegos.stock import Videojuegos  # Importa la clase Videojuegos
from moviles.tipos_de_moviles import Moviles  # Importa la clase Moviles
from consolas.tipos_de_consolas import Consolas  # Importa la clase Consolas
from ordenadores.tipos_de_ordenadores import Ordenadores  # Importa la clase Ordenadores

class Catalogo:
    def mostrar_opciones(self):
        print("\nBienvenido al catálogo. ¿Qué deseas ver?")
        opciones = ["1. Videojuegos", "2. Móviles", "3. Consolas", "4. Ordenadores"]
        for opcion in opciones:
            print(opcion)

        eleccion = input("Selecciona una opción (1-4): ").strip()
        if eleccion == "1":
            videojuegos = Videojuegos()  # Instancia de la clase Videojuegos
            videojuegos.mostrar_categorias()  # Llama al método para mostrar categorías
        elif eleccion == "2":
            moviles = Moviles()  # Instancia de la clase Moviles
            moviles.mostrar_opciones()  # Llama al método para mostrar opciones de móviles
        elif eleccion == "3":
            consolas = Consolas()  # Instancia de la clase Consolas
            consolas.mostrar_opciones()  # Llama al método para mostrar opciones de consolas
        elif eleccion == "4":
            ordenadores = Ordenadores()  # Instancia de la clase Ordenadores
            ordenadores.mostrar_opciones()  # Llama al método para mostrar opciones de ordenadores
        else:
            print("Opción no válida. Intenta nuevamente.")