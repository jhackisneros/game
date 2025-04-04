from flask import Flask, render_template, request, redirect, url_for
from catalogo.catologo_de_todo import Catalogo
from videojuegos.stock import Videojuegos
from moviles.tipos_de_moviles import Moviles
from consolas.tipos_de_consolas import Consolas
from ordenadores.tipos_de_ordenadores import Ordenadores

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/catalogo")
def catalogo():
    return render_template("catalogo.html")

@app.route("/videojuegos")
def videojuegos():
    videojuegos = Videojuegos()
    categorias = videojuegos.categorias
    return render_template("videojuegos.html", categorias=categorias)

@app.route("/moviles")
def moviles():
    moviles = Moviles()
    android = moviles.android
    apple = moviles.apple
    return render_template("moviles.html", android=android, apple=apple)

@app.route("/consolas")
def consolas():
    consolas = Consolas()
    xbox = consolas.xbox
    playstation = consolas.playstation
    return render_template("consolas.html", xbox=xbox, playstation=playstation)

@app.route("/ordenadores")
def ordenadores():
    ordenadores = Ordenadores()
    nvidia = ordenadores.nvidia
    amd = ordenadores.amd
    return render_template("ordenadores.html", nvidia=nvidia, amd=amd)

if __name__ == "__main__":
    app.run(debug=True)