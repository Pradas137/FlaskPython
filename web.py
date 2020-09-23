from flask import Flask
app = Flask(__name__)
 
from flask import render_template
from flask import request
from flask import current_app
import random

file = open("equips.cfg","r")
equipos= file.read().splitlines()
listaEquipos =[]
Ligas ={}
diccLigas = {}
diccMostrar = {}
Lista=[]

def PuntosResultados():
    puntos1 = random.randint(0, 9)
    puntos2 = random.randint(0, 9)
    return (puntos1, puntos2)

def partido():
    file = open("equips.cfg", "r")
    datos = file.read().splitlines()
    file.close()

    equipos = []
    for Local in datos:
        for Visitantes in datos:
            if Local != Visitantes:
                equipos.append(Visitantes)
    Liga=[]
    Ligas ={}
    for Local in range(0, len(datos)):
        Lista = []
        for Visitantes in range(1, len(datos)):
            diccionario1 = {}
            diccionario1[equipos[0]] = "none"
            del equipos[0]
            Lista.append(diccionario1)
            Ligas[str(datos[Local])] = Lista
    return (Ligas)


def añadiryMostrar(Partidos):
    diccionario2 = {}
    for Local in Partidos:
        for Visitantes in Partidos[Local]:
            reultado = PuntosResultados()
            for puntos in Visitantes:
                diccionario2[puntos] = reultado
            Visitantes.update(diccionario2)

    equips = open("equips.cfg", "r")
    datos = equips.read().splitlines()
    for j in range(1,len(datos)):
        datos[j] = {datos[j] : 0}
    equips.close()
    for Local in Partidos:
        for pe in Partidos[Local]:
            for Visitante in pe:
                print("|",Local, "       |     \tcontra      ","|     ", Visitante, "|", pe.get(Visitante))


Partidos=partido()   
Final = añadiryMostrar(Partidos)


@app.route('/')
def Menu():
        return render_template('Menu.html')

@app.route('/Equipos')
def Equipos_get():
        return render_template('Equipos.html', equipos=equipos)

@app.route('/Partidos')
def Partidos_get():

	return render_template('Partidos.html', equipos=equipos, Lista=Lista, listaEquipos=listaEquipos, Ligas=Ligas, Final=Final)

@app.route('/Equipos',methods=["POST"])
def Equipos_post():

    return render_template('Equipos.html',
                producte=producte, quantitat=quantitat)


@app.route('/Partidos',methods=["POST"])
def Partidos_post():

    return render_template('Partidos.html',
                producte=producte, quantitat=quantitat)
  
# arranquem l'aplicació
app.run( debug=True )