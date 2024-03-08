from flask import Flask, request, jsonify, render_template, redirect, url_for
app = Flask(__name__)

# http://localhost:8081/login
@app.route("/login", methods=["GET", "POST"])
def login():
    #Se dan los valores ingresados de username y password
    if request.method == "POST":
        #username = request.form["username"].capitalize() esta ayuda a poner la primera letra en mayusculas
        username = request.form["username"]
        password = request.form["password"]
        #valida los datos de username con la primera letra en mayuscula
        # y password con la condicion de que sea alfanumerica valida letras y numeros
        if username[0].isupper() and password.isalnum() and any(c.isalpha() for c in password) and any(c.isdigit() for c in password):
            return redirect(url_for("login_success"))
        else:
            #Si no cumple las especificaciones se mantiene en login
            return redirect(url_for("login"))
    #muestra el html de inicio
    return render_template("inicio.html")

#muestra el mensaje de bienvenida
@app.route("/login_sucessful")
def login_success():
    return render_template("ingreso.html")


# http://localhost:8081/hello
@app.route("/hello", methods=["GET"])
def hello():
    return "Hello World!"


# http://localhost:8081/params?test=Mario
@app.route("/params", methods=["GET"])
def params():
    test = request.args.get("test", default="World", type=str)
    return f"Hello {test}"


# http://localhost:8081/mario
@app.route("/name/<name>", methods=["GET"])
def root(name: str):
    return f"Hello {name}"


@app.route('/test', methods=['POST'])
def my_view_func():
    email = request.form.get('email')
    password = request.form.get('password')
    return f"Hello {email}"


@app.route('/json', methods=["POST"])
def json():
    data = request.get_json()
    return jsonify(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8081)
