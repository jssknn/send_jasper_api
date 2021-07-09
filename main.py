from flask import Flask, render_template, request, redirect, session, flash
import requests
app = Flask(__name__)
app.secret_key = ''

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/enviar_comandos", methods=["POST"])
def enviar_comandos():
    iccds = request.form["iccds"]
    comandos = request.form["comandos"]
    listaIccds = iccds.split (",")
    listaComandos = comandos.split ("|")
    headers = {
    'Content-Type': "application/json",
    'Accept': "application/json",
    'Authorization': "",
    'Cache-Control': "no-cache",
    'Postman-Token': ""
    }
    for numero in listaIccds:
        url = "https://restapi1.jasper.com/rws/api/v1/devices/"+numero+"/smsMessages"
        for comando in listaComandos:
            payload = "{\r\n\"messageText\":\""+comando+"\"\r\n}"
            response = requests.request("POST", url, data=payload, headers=headers)

    flash("Comandos enviados: " + comandos)        
    flash("Numeros: " + iccds)   
    return redirect("/")


# Iniciar el servidor
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)