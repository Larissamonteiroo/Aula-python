from flask import Flask, request, render_template

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        n1 = 43
        n2 = 76
        soma = n1 + n2

        return render_template('index.html', var1 = soma, var2 = "Laríssa")

    @app.route("/produtos")
    def produtos():
        x = request.args.get("id")
        y = request.args.get("nome")

        return f"<h1>Lista de produtos</h1> <p>Seu id é: {x} e seu nome é: {y}</p>"

    return app


app = create_app()

app.run(debug=True, port=2000, host="localhost")