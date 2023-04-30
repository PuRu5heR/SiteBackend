from flask import Flask, render_template, redirect, flash, url_for
from castles_database import CastleDB

app = Flask("World Castles")


@app.route("/")
def index():
    castles_list = CastleDB().get_castles()
    for castle in castles_list:
        print(castle[4])
    return render_template("index.html", castles=castles_list)


@app.route("/castles/<castle_src>")
def castles(castle_src):
    castles_list = CastleDB().get_castles()
    castle = get_castle(castle_src)
    return render_template("castles.html", castles=castles_list, castle=castle)


if __name__ == "__main__":
    app.run(host="192.168.58.2", debug=True)
