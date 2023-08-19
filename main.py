# chame a biblioteca do Flask
from flask import Flask, render_template
# crie uma variável para chamar o Flask, é recomendada q ela seja chamada de app
app = Flask(__name__)

# criar a 1 pagina do site
# route (o que vem depois da barra) -> meusite.com/contatos
# função -> o que voce quer exibir naquela página
# template

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)




# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)