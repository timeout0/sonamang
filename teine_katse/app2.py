from flask import Flask, render_template, session, redirect, url_for, request


app = Flask(__name__)




@app.route("/", methods=["POST","GET"])
def home():
    if request.method=="POST":
        difficulty = request.form.get("diff")
        print(difficulty)
        return redirect(url_for("game",diff=difficulty))
    return render_template("home.html")


@app.route("/game")
def game():
    diff = request.args.get("diff")
    return render_template("game.html",diff=diff,wordlist=["tere","headaega","meelis"])


if __name__=="__main__":
    app.run(debug=True)
