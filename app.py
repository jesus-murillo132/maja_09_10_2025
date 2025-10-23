from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('mi_plantilla.html', creador="Murillo Arroyo Jesus Alejandro")

@app.route('/animales_exoticos')
def animales_exoticos():
    return render_template('animales_exoticos.html', creador="Murillo Arroyo Jesus Alejandro")

@app.route('/animales_terrestres')
def animales_terrestres():
    return render_template('animales_exoticos.html', creador="Murillo Arroyo Jesus Alejandro")

@app.route('/autos_antiguos')
def autos_antiguos():
    return render_template('autos_antiguos.html', creador="Murillo Arroyo Jesus Alejandro")

@app.route('/las_maravillas_del_mundo')
def maravillas():
    return render_template('las_7_maravillas.html', creador="Murillo Arroyo Jesus Alejandro")

@app.route('/acerca_de')
def acerca_de():
    return render_template('acerca_de.html', creador="Murillo Arroyo Jesus Alejandro")

@app.route('/inicio_de_sesion', methods=['GET', 'POST'])
def inicio_de_sesion():
    if request.method == 'POST':
        return redirect(url_for('inicio'))
    return render_template('inicio_de_sesion.html', creador="Murillo Arroyo Jesus Alejandro")

if __name__ == '__main__':
    app.run(debug=True)
