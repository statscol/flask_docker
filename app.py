from flask import Flask
from flask import render_template
from flask import request,url_for,redirect
import os
from datetime import datetime
import numpy as np

###request python 
import subprocess
import requests

app=Flask(__name__)

@app.route("/")
def home():
	return str(datetime.now())
@app.route("/ced/<id>",methods=["GET","POST"])
def cedula(id):
	return f"your id is {id}"

if __name__ == "__main__":
	app.run(debug=True,host="0.0.0.0",port=5001)