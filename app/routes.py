from flask import Flask, render_template, session
from app import app
import random


colors = ["red", "blue"]

@app.route('/')
@app.route('/index')
def setColor():
    if "color" not in session:
        color = random.choice(colors)
        session["color"] = color

    return render_template("index.html", session=session)

@app.route('/reset')
def resetColor():
    if "color" in session:
        session.pop("color")

    return "Color Reset"

if __name__ == '__main__':
    app.run()