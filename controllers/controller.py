import pdb
from threading import settrace
from flask import render_template
from app import app
from models.game_list import *
from models.game import *
from models.player import *


@app.route('/')
def index():
    return "Hello World"

# pdb.set_trace()
@app.route('/<p1move>/<p2move>')
def results(p1move,p2move):
    return render_template('index.html', p1move = p1move, p2move = p2move)

@app.route('/new_game', methods=["POST"])
def play_game():
