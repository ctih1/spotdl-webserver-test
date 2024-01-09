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
    subprocess.call(f"spotdl {request.args['url']}", cwd="/media/files/music")
    return render_template("download.html")

app.run(port=8080)