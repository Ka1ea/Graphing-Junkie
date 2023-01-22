from datetime import datetime

from flask import Flask, render_template, request, url_for, redirect

from src import app, cursor, connection
import json


def db_get_all():
    cursor.execute('SELECT * FROM colorwars')
    results = cursor.fetchall()
    return results


def db_get_by_id(id):
    cursor.execute('SELECT * FROM colorwars WHERE colorgroup = %s', (id, ))
    result = cursor.fetchone()
    return result



def db_update_group(team):
    cursor.execute("UPDATE colorwars SET score = ISNULL(ID, 0) + 1 WHERE colorgroup = %s")
    connection.commit()



@app.route("/", methods=['GET', 'POST'])
def home():
    results = db_get_all()
    print(results)
    rval, gval, bval = [x[-1] for x in results]
    return render_template("barClicker.html", 
                           rclicks = rval,
                           gclicks = gval, 
                           bclicks = bval)


@app.route("/update", methods=['POST']) 
def update(): 
    print(json.loads(request.data.decode()))
    # data = json.loads(request.data.decode())[0]
    # print("updated  " + data )
    # db_update_group(data)
        

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