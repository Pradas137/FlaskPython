from __future__ import print_function

from flask import Flask
app = Flask(__name__)

from collections import OrderedDict
from flask import render_template
from flask import request
from flask import current_app
import random
import logging
import sys

from collections import OrderedDict

def file():
    file = open("equips.cfg", "r")
    datos = file.read().splitlines()
    file.close()
    return datos

def partido(file):
    equipos = []
    for Local in file:
       # print(Local)
        for Visitantes in file:
            # print(Visitantes)
            if Local != Visitantes:
                equipos.append(Visitantes)
                #print(equipos) 
    Ligas ={}
    for Local in range(0, len(file)):
        Lista = []
        # print(Local)
        for Visitantes in range(1, len(file)):
            # print(Visitantes)
            diccionario1 = {}
            diccionario1[equipos[0]] = "none"
            del equipos[0]
            Lista.append(diccionario1)
            #print(Lista)
            Ligas[str(file[Local])] = Lista
    return (Ligas)

def PuntosResultados():
    puntos1 = random.randint(0, 9)
    puntos2 = random.randint(0, 9)
    return (puntos1, puntos2)

def añadir(Partidos):
    for Local in Partidos:
        # print(Local)
        for Visitantes in Partidos[Local]:
            # print(Visitantes)
            reultado = PuntosResultados()
            for puntos in Visitantes:
                temp={}
                temp[puntos] = reultado
            Visitantes.update(temp)
    return(Partidos)

def Mostrar(Partidos):
    equips = open("equips.cfg", "r")
    datos = equips.read().splitlines()
    for j in range(0, len(datos)):
        datos[j] = {datos[j]: 0}
    equips.close()
    for Local in Partidos:
        #print(local)
        for pe in Partidos[Local]:
            # print(pe)
            for i in pe:
                lo = (Local, i, (pe.get(i)))
            print(lo)


file=file()
Partidos = partido(file)
add= añadir(Partidos)
mostrar= Mostrar(add)

@app.route('/')
def Menu():
        return render_template('Menu.html')

@app.route('/Equipos')
def Equipos_get():
    data = [['Valencia',[['Betis', (6, 0)],['Madrid', (2, 7)],['Sevilla',(3, 7)]]],['Betis',[['Valencia', (3, 7)],['Madrid',  (7, 3)],['Sevilla',(8, 6)]]]]
    return render_template('Equipos.html',Partidos=Partidos,file=file,mostrar=mostrar,data=data)

@app.route('/Partidos')
def Partidos_get():

	return render_template('Partidos.html',Partidos=Partidos)

@app.route('/Ranking')
def Ranking_get():
        return render_template('Ranking.html',Partidos=Partidos)


@app.route('/Equipos',methods=["POST"])
def Equipos_post():
    return render_template('Equipos.html',producte=producte, quantitat=quantitat)


@app.route('/Partidos',methods=["POST"])
def Partidos_post():

    return render_template('Partidos.html',producte=producte, quantitat=quantitat)
  
# arranquem l'aplicació
app.run( debug=True )