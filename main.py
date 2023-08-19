from flask import Flask

app = Flask(__name__)

# criar a 1 pagina do site
# route (o que vem depois da barra) -> hashtagtreinamentos.com/contatos
# função -> o que voce quer exibir naquela página
# template

@app.route("/")
def homepage():
    return "Esse é o meu primeiro site, a homepage"

@app.route("/contatos")
def contatos():
    return "<p>Nossos contatos são:</p> <p>email: blablabla@gmail.com</p> <p>telefone: (11)99999-9999</p>"



# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)