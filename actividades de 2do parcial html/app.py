from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('mi_plantilla.html',creador="Murillo Arroyo Jesus Alejandro")


@app.route('/autos antiguos')
def index():
    return render_template('autos antiguos.html',creador="Murillo Arroyo Jesus Alejandro")

@app.route('/las maravillas del mundo')
def index():
    return render_template('las 7 maravillas.html',creador="Murillo Arroyo Jesus Alejandro")

@app.route('/aserca de')
def index():
    return render_template('aserca_de.html',creador="Murillo Arroyo Jesus Alejandro")


if __name__ == '__main__':
    app.run(debug=True)
