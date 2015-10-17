import logging

from flask import Flask, render_template

log = logging.getLogger(__name__)
app = Flask(__name__)

def boot():
	log.debug("Booting HTTP API")
	app.debug = True
	app.run()

@app.route("/")
def index():
	return render_template("hello.html")