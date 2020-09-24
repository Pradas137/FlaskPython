from __future__ import print_function

from flask import Flask
app = Flask(__name__)

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



file=file()
Partidos = partido(file)

@app.route('/')
def Menu():
        return render_template('Menu.html')

@app.route('/Equipos')
def Equipos_get():
        return render_template('Equipos.html',file=file)

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