from datetime import datetime

from flask import Flask, render_template, request, jsonify, redirect, url_for

from src import app
import json

numusers = 0
winval = 100
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
@app.route("/<error>")
def home(error=None):
    return render_template("basecamp.html",
                           error=error)
    
@app.route("/game")
@app.route("/game/<gamename>", methods=["GET"]) 
def game(gamename=None):
    if(gamename == None or gamename == "" or (gamename not in scores)) :
        return render_template("error.html",  error= "<" + gamename + ">" + " is not a game :(")
    
    rval, gval, bval = [0,0,0]

    try:
        rval, gval, bval = [x for x in scores[gamename]["scores"].values()]
    except:
        return render_template("error.html", error=gamename)

    print(rval)

    if (rval > winval or gval > winval or bval > winval) :
        score_vals= scores[gamename]["scores"]
        winner = "r"
        if (score_vals["g"] == winval):
            winner = "g" 
        elif (score_vals["b"] == winval):
            winner = "b"    
        return redirect(url_for("end"), end=winner)
    

    return render_template("barClicker.html",
                           gamename=gamename,
                           rclicks=rval,
                           gclicks=gval,
                           bclicks=bval)

@app.route("/startgame", methods=['POST'])
def startgame():
    result = request.form.get("gamename")
    if (result in scores):
        return redirect(url_for('home', error="game name taken or invalid game name"))
    scores[result] = {
        "scores": {
            "r": 1,
            "g": 1,
            "b": 1
        },
        "timeout" : 3600
    }
    return redirect(url_for('game', gamename=result))

@app.route("/update", methods=['POST'])
def update():
    id = json.loads(request.data.decode())["id"]
    gamename = json.loads(request.data.decode())["gamename"]
    scores[gamename]["scores"][id] = scores[gamename]["scores"][id] + 1
    if scores[gamename]["scores"][id] > winval:
        return jsonify(id)
    
    # print(id, gamename)
    # print(scores[gamename])
    return jsonify(scores[gamename]["scores"])

# @app.route("")
@app.route("/end/<end>")
def end(end=None):
    return render_template("victory.html", end=end)


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
