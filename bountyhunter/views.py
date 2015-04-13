from bountyhunter import app
from bountyhunter import db
from bountyhunter import models
from flask import render_template

@app.route('/')
def index():
    requests = models.Request.query.filter(models.Request.bandcamp != None).all()
    return render_template('index.html', requests=requests, count=len(requests))
