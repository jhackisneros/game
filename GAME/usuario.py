from catalogo.catologo_de_todo import Catalogo  # Importa la clase Catalogo

class UsuarioGame:
    def __init__(self):
        self.usuarios_registrados = {}  # Diccionario para almacenar usuarios registrados

    def iniciar(self):
        print("¡Hola! Bienvenido al Game.")
        while True:
            es_usuario = input("¿Eres usuario del Game? (sí/no): ").strip().lower()

            if es_usuario == "sí":
                correo = input("Por favor, ingresa tu correo: ").strip()
                contraseña = input("Por favor, ingresa tu contraseña: ").strip()

                if self.verificar_usuario(correo, contraseña):
                    print("¡Acceso concedido! Bienvenido de nuevo.")
                    self.mostrar_catalogo()  # Llama al catálogo
                    break
                else:
                    print("Correo o contraseña incorrectos. Intenta nuevamente.")
            elif es_usuario == "no":
                desea_registrarse = input("¿Te gustaría registrarte? (sí/no): ").strip().lower()

                if desea_registrarse == "sí":
                    self.registrar_usuario()
                else:
                    print("Has ingresado como invitado. ¡Disfruta del juego!")
                    self.mostrar_catalogo()  # Llama al catálogo
                    break
            else:
                print("Opción no válida. Por favor, intenta nuevamente.")

    def mostrar_catalogo(self):
        catalogo = Catalogo()
        catalogo.mostrar_opciones()

    def verificar_usuario(self, correo, contraseña):
        # Verifica si el correo y la contraseña coinciden con un usuario registrado
        return self.usuarios_registrados.get(correo) == contraseña

    def registrar_usuario(self):
        print("¡Perfecto! Vamos a registrarte.")
        correo = input("Dime un correo: ").strip()
        contraseña = input("Crea una contraseña: ").strip()

        if correo in self.usuarios_registrados:
            print("Este correo ya está registrado. Intenta iniciar sesión.")
        else:
            self.usuarios_registrados[correo] = contraseña
            print("¡Registro exitoso! Ahora puedes iniciar sesión.")