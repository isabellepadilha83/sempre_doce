from flask import Flask, render_template,request, redirect,url_for

app = Flask(__name__)

@app.route("/")
def inicial():
    return render_template("index.html")

@app.route("/menu")
def menu():
    return render_template("menu.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/login", methods=["get", "post"])
def login():
    if request.method == "get":
        return render_template("login.html")
    elif request.method == "post":
        usuario = request.form.get("username")
        senha= request.form.get("password")

        if usuario == "usuario1":
            if senha == "senhaUsuario":
                return redirect(url_for('upload'))

@app.route("/upload")
def upload ():
    return render_template("upload.html")    
        
    
if __name__ == '__main__':
    app.run(debug=True)
