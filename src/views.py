from datetime import datetime

from flask import Flask, render_template, request, jsonify, redirect, url_for

from src import app
import json

numusers = 0
scores = {
    "testgame": {
        "scores": {
            "r": 1,
            "g": 1,
            "b": 1
        },
        "timeout" : 3600
    }
}


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("basecamp.html")
    
@app.route("/game/<gamename>", methods=["GET"]) 
def game(gamename=None):
    if(gamename == None or gamename == "" or not scores.has_key(gamename)) :
        return render_template("error.html", error=gamename)
    
    rval, gval, bval = [0,0,0]

    try:
        rval, gval, bval = [x for x in scores[gamename]["scores"].values()]
    except:
        return render_template("error.html", error=gamename)

    print(rval)

    if (rval > 100 or gval > 100 or bval > 100) :
            return redirect(url_for("/end"))
    

    return render_template("barClicker.html",
                           rclicks=rval,
                           gclicks=gval,
                           bclicks=bval)

@app.route("/startgame", methods=['POST'])
def startgame():
    result = json.loads(request.data.decode())["gamename"]
    scores[result] = {
        "scores": {
            "r": 1,
            "g": 1,
            "b": 1
        },
        "timeout" : 3600
    }
    return redirect(url_for('game/' + result))

@app.route("/update", methods=['POST'])
def update():
    result = json.loads(request.data.decode())["id"]
    scores[result] = scores[result] + 1
    return jsonify(scores)

@app.route("/end")
def get_end():
    return render_template("end.html")


@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/contact/")
def contact():
    return render_template("contact.html")


@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name=None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )


@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")
