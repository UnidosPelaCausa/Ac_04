from flask import Flask 

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Tente trocar a url para participantes"

@app.route("/participantes")
def grupo():
    return '''<p>Henrique Almeida Silva - RA 2202055</p>
<p>Matheus Marques Matos de Oliveira - RA 2201538</p>
<p>Filipe Dourado Pereira  - RA 2202115</p>
<p>Rodrigo Antony Oliveira Maia - RA 2201647</p>
<p>Vitor Gabriel Pereira Becker - RA 2202237</p>'''

if __name__ == "__main__":
    app.run(debug=True)