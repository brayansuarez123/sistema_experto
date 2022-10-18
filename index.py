from flask import Flask, render_template, request
from numpy import array

index = Flask(__name__)

@index.route("/")
def hello_world():
    return render_template("plantilla.html")

@index.route("/sistema",methods=["POST"])
def devolver():
    print(request.form)
    return render_template("plantilla.html")

def recibir(**fromdata):
    print(fromdata)
    return

if __name__ == "__main__":
    index.run()