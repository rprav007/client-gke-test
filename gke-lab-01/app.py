# The Docker image contains the following code
from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def showPinehead():
    html = "<div style='text-align:center;margin:20px;'><h1>Greetings from Google Cloud!</h1><img src='https://images.idgesg.net/images/article/2018/07/google-cloud-services-100765812-large.jpg'></div>"
    return html

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80)
