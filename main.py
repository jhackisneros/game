import os
from GAME.usuario import UsuarioGame  # Importa la clase UsuarioGame

if __name__ == "__main__":
    print(os.path.basename(os.path.dirname(__file__)))

    # Instancia de UsuarioGame e inicia el programa
    usuario_game = UsuarioGame()
    usuario_game.iniciar()