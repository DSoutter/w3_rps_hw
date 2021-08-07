from flask import render_template, request, redirect
from app import app
from models.game_list import *
from models.game import *
from models.player import *

@app.route('/home')
def index():
    return render_template('home.html')

@app.route('/<p1move>/<p2move>')
def results(p1move,p2move):
    return render_template('index.html', p1move = p1move, p2move = p2move)

@app.route('/game')
def new_game():
    return render_template('input.html')

@app.route('/winner', methods=['POST'])
def play_game():
    name1 = request.form['p1_name']
    choice1 = request.form['p1_choice']
    name2 = request.form['p2_name']
    choice2 = request.form['p2_choice']
    player1=Player(name1,choice1)
    player2=Player(name2,choice2)
    winner = Game.game_on(player1, player2)
    return render_template('winner.html', winner = winner, player1=player1,player2=player2)
