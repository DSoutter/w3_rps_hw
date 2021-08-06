from models import player
from models.game_list import *
from models.game import *
from models.player import *
from flask import render_template
from app import app

@app.route('/')
def index():
    return "Hello World"
@app.route('/<player1>/<player2>')

def results(player1,player2):
    return render_template('results.html', result=Game.game_on)
