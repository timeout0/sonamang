from flask import Flask, render_template, request, jsonify, url_for, redirect
import threading
import random
import time

limit = 2
words = ["tere", "headaega", "tore", "maailm"]
gamewords = []
game_started = False
score = 0
continue_thread = True
game_began = False

app = Flask(__name__)

def update_gamewords():
    global gamewords, continue_thread
    while continue_thread:
        time.sleep(3)
        if len(gamewords) <= limit:
            gamewords.append(random.choice(words))
        
            
@app.route("/")
def index():
    return render_template("index.html")

@app.route('/get_gamewords')
def get_gamewords():
    global gamewords, limit
    if len(gamewords) > limit:
        gamewords = []
        return jsonify({'game_over': True})
    else:
        return jsonify({'game_over': False, 'gamewords': gamewords})

@app.route("/game_over")
def game_over():
    global score, game_began, continue_thread
    continue_thread = False
    game_began = False
    return render_template("game_over.html", score=score)

@app.route('/game', methods=["GET", "POST"])
def game():
    global gamewords, game_began, game_started, continue_thread, score
    if not game_began:
        game_began = True
        continue_thread = True
        gamewords = []
    if not game_started:
        game_started = True
        threading.Thread(target=update_gamewords, daemon=True).start()
    
    title = "SONAMANG"
    if request.method == "POST":
        typed_word = request.form.get("typedWord")

        if typed_word.lower() in gamewords:
            message = "Correct!"
            gamewords.remove(typed_word.lower())
            score += 1
        else:
            message = "Incorrect, try Again!"

        return render_template("game.html", gamewords=gamewords, message=message, title=title)

    gamewords.append(random.choice(words))
    return render_template("game.html", gamewords=gamewords, title=title)

if __name__ == '__main__':
    app.run(debug=True)
