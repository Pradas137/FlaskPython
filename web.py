from flask import Flask, request, redirect, url_for, render_template
app = Flask(__name__)




def Equipos():
    """Load teams and append to list from file."""
    Lista_equipos = []
    file = open("equips.cfg", "r")
    for equips in file:
        Lista_equipos.append(equips.rstrip("\n"))
    return Lista_equipos


def CrearLiga():
    """ Creates the league matrix."""
    Liga = {}
    for Local in equips:
        Liga[Local] = {}
        for Visitante in equips:
            if Visitante == Local:
                Liga[Local][Visitante] = "X"
            else:
                Liga[Local][Visitante] = ""
    return Liga

def update_league(Local, Visitante, GolesL, GolesV):
    """Update goals on the league matrix."""
    Ligas[Local][Visitante] = GolesL
    Ligas[Visitante][Local] = GolesV


equips = Equipos()
Ligas = CrearLiga()


@app.route('/')
def Menu():
    return render_template("Menu.html")

@ app.route('/Equipos')
def Lista_equipos():
    return render_template("Equipos.html", equips=equips)

@ app.route('/Partidos')
def Partidos():
    return render_template("Partidos.html", Ligas=Ligas, equips=equips)

        
