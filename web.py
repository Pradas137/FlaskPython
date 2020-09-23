from flask import Flask
app = Flask(__name__)
 
from flask import render_template
from flask import request
from flask import current_app


file = open("equips.cfg","r")
equipos= file.read().splitlines()
listaEquipos =[]
Ligas ={}
diccLigas = {}
Lista=[]

@app.route('/')
def Menu():
        return render_template('Menu.html')

@app.route('/Equipos')
def Equipos_get():
        return render_template('Equipos.html', equipos=equipos)

@app.route('/Partidos')
def Partidos_get():

	return render_template('Partidos.html', equipos=equipos, Lista=Lista, listaEquipos=listaEquipos, Ligas=Ligas, diccLigas=diccLigas)

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