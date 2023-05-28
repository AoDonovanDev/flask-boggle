from boggle import Boggle
from flask import Flask, render_template, request, session, flash, jsonify, make_response
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "!1IcedCoffee"

debug = DebugToolbarExtension(app) 

boggle_game = Boggle()


@app.route('/')
def new_game():
    """ render game board, check if there is a high schore to display """
    board = boggle_game.make_board()
    session['board'] = board
    if 'score' in session:
        return render_template('base.html', highScore = session['score'], count = session['count'], board=board)
    return render_template('base.html', board = board)

@app.route('/guess', methods = ["post"])
def guess():
    """ check if guess is valid and return result """
    board = session['board']
    guess = request.form['guess']
    print(guess)
    msg = boggle_game.check_valid_word(board, guess)
    return {'result': msg}

@app.route('/end', methods = ["post"])
def end():
    """ add to session count and update high score if needed """
    score = int(request.form['score'])
    if 'score' in session:
        if score > session['score']:
            session['score'] = score
    else:
        session['score'] = score
    if 'count' in session:
        count = session['count']
        session['count'] = count + 1
    else:
        session['count'] = 1
    print(session['count'])
    print(session['score'])

    return {'count': session['count'], 'highScore': session['score']}