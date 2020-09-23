from flask import Flask
app = Flask(__name__)
 
from flask import render_template
from flask import request
from flask import current_app


productes =["melon","sandia","platanos"]

file = open("equips.cfg","r")
lliga= file.read().splitlines()


@app.route('/compra')
def compra_get():
        return render_template('compra_form.html', productes = productes, liga= Lliga)

 
@app.route('/compra',methods=["POST"])
def compra_post():

    return render_template('compra_post.html',
                producte=producte, quantitat=quantitat)
    
# arranquem l'aplicació
app.run( debug=True )