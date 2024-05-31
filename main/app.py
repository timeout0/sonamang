
from flask import Flask, render_template, session, redirect, url_for, request


app = Flask(__name__)
app.config["SECRET_KEY"] = "xxx"

@app.route("/", methods=["POST","GET"])
def home():
    if request.method=="POST":
        difficulty = request.form.get("diff")
        session["diff"] = difficulty
        return redirect(url_for("game"))
    score = session.get("score","0")
    with open("scores1.txt","r") as f:
        scores1 = sorted([int(x) for x in f.read().split(",")[:-1]],)[::-1]
    with open("scores2.txt","r") as f:
        scores2 = sorted([int(x) for x in f.read().split(",")[:-1]],)[::-1]
    with open("scores3.txt","r") as f:
        scores3 = sorted([int(x) for x in f.read().split(",")[:-1]],)[::-1]
    return render_template("home.html",score=score,scores1=scores1,scores2=scores2,scores3=scores3)


@app.route("/game", methods=["POST","GET"])
def game():
    if request.method=="POST":
        score = request.form.get("score")
        session["score"] = score
        diff = session.get("diff","1")
        with open("scores"+diff+".txt","a") as f:
            f.write(score+",")
        return redirect(url_for("home"))
    diff = session.get("diff","1")
    with open("lst"+diff+".txt", encoding="utf-8") as f:
        wordlist = f.read().split("\n") 
    return render_template("game.html",diff=diff,wordlist=wordlist)


if __name__=="__main__":
    app.run(debug=True)
