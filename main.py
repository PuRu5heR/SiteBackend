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
    castle = CastleDB().get_castle(castle_src)
    castle_text = CastleDB().get_castle_text(castle[0])
    castle_images = CastleDB().get_castle_images(castle[0])
    return render_template("castles.html", castles=castles_list, castle_text=castle_text, castle_images=castle_images,
                           length=len(castle_text))


if __name__ == "__main__":
    app.run(host="192.168.1.132", debug=True)
