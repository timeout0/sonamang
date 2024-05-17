from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)




@app.route("/", methods=["POST","GET"])
def home():
    return render_template("home.html")




@app.route("/home", methods=["POST"])
def submit(player_name, score):
    player_name = request.form["input_playername"]
    score = request.form["input_playerscore"]
    session['stored_player_name'] = player_name
    session['stored_score'] = score
    with open("highscores_and_usernames", "a") as file:
        file.write("\n", player_name, score)

if __name__=="__main__":
    app.run(debug=True)
