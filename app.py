from flask import Flask, render_template, request
import random

words = ["tere", "headaega", "tore", "maailm"]

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    title = "SONAMANG"
    if request.method == "POST":
        typed_word = request.form.get("typedWord")
        correct_word = request.form.get("correctWord")

        if typed_word.capitalize() == correct_word.capitalize():
            message = "Correct!"
            word = random.choice(words)
        else:
            message = "Incorrect, try Again!"
            word = correct_word

        
        return render_template("index.html", word=word, message=message,title=title)

    word = random.choice(words)
    return render_template("index.html", word=word, title=title)

if __name__ == '__main__':
    app.run(debug=True)
