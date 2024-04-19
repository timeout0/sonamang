from flask import Flask, render_template, request
import random

words = ["tere", "headaega", "tore", "maailm"]

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        typed_word = request.form.get("typeWord")
        correct_word = request.form.get("correctWord")

        if typed_word == correct_word:
            message = "Correct!"
            word = random.choice(words)
        else:
            message = "Incorrect, try Again!"
            word = correct_word

        
        title = "Kirjuta " + word.capitalize()
        return render_template("index.html", word=word, message=message,title=title)

    word = random.choice(word)
    title = "Kirjuta " + word.capitalize()
    return render_template("index.html", word=word, title=title)

if __name__ == '__main__':
    app.run(debug=True)
