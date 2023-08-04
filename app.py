
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
# def Inicio():
    #texto={'titulo':'Pagina de inicio','saludo':'Bienvenido a la pagina web','principal':'listas'}
    #palabra=['jhon','rosita','kimberly','aily']
    #return render_template('inicio.html',data=texto,palabra=palabra)
def Inicio():
    return
if __name__== '__main__':
    app.run(debug=True)