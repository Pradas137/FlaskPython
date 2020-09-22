from flask import Flask
app = Flask(__name__)
 
from flask import render_template
from flask import request
from flask import current_app


@app.route('/')
def hello_world():
    return 'Hello, World!'


productes =["melon","sandia","platanos"]

file = open("equips.cfg","r")
lliga= file.read().splitlines()


@app.route('/compra')
def compra_get():
        return render_template('compra_form.html', productes = productes)

 
@app.route('/compra',methods=["POST"])
def compra_post():

    return render_template('compra_post.html',
                producte=producte, quantitat=quantitat, lliga= Lliga)
    
# arranquem l'aplicació
app.run( debug=True )