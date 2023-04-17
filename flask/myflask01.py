#!/usr/bin/python3
# An object of Flask class is our WSGI application
from flask import Flask


app = Flask(__name__)

@app.route("/hello")
def hello_world():
   return "Hello World"

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224)
   # app.run(host="0.0.0.0", port=2224, debug=True) # DEBUG MODE
                                                          
~    
