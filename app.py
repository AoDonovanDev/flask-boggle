from boggle import Boggle
from flask import Flask, render_template, request, session

app = Flask(__name__)
app.config['SECRET_KEY'] = "!1IcedCoffee"

boggle_game = Boggle()

@app.route('/')
def new_game():
    board = boggle_game.make_board()
    session['board'] = board
    return render_template('base.html', board = board)

@app.route('/guess', methods = ["POST"])
def guess():
    print(request.data)
    return render_template('base.html', board = session['board'])