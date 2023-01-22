from datetime import datetime

from flask import Flask, render_template, request, url_for, redirect

from src import app
import json

scores = {
    "r" : 1,
    "g" :1,
    "b" :1
}



@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        print("tes2t")
        result = json.loads(request.data.decode())["id"]
        scores[result] = scores[result] + 1
        return scores
    
    rval, gval, bval = [x for x in scores.values()]
    print(rval)
    return render_template("barClicker.html", 
                           rclicks = rval,
                           gclicks = gval, 
                           bclicks = bval)


# @app.route("/update", methods=['POST']) 
# def update(): 
    
#     # data = json.loads(request.data.decode())[0]
#     # print("updated  " + data )
#     # db_update_group(data)
        

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")