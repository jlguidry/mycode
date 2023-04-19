#!/usr/bin/python3

from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template

#create flask instance
app = Flask(__name__)

#get username
@app.route("/")
@app.route("/enter_name")
def enter_name():
    return render_template("enter_name.html")

#greet user
@app.route("/greet_user" methods = ["POST", "GET"]) 
def greet_user():
    if request.method == "POST":
        if request.form.get("user"):
            user = request.form.get("user")
        else:
            user = "default user"
    return render_template("greet_user.html", user=user)

#ask order
@app.route("/serve", methods = ["POST"])
def server():
    if request.method == "POST":
       if request.form.get("order")
           order = request.form.get("order")
        else:
            order = "nothing"
    return render_template("serve.html", order=order)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
