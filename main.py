from flask import Flask
from flask import render_template
from flask import request
import subprocess
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/download")
def download():
    subprocess.call(f"spotdl {request.args['url']}", shell=True, cwd="/media/files/music")
    return render_template("download.html")

app.run(host="192.168.100.45", port=8080)