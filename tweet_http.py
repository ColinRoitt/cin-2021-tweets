"""
    URY Tweet Board
    Candidate Interview Night 2021

    Author: Michael Grace
    Date: November 2020

    github.com/UniversityRadioYork

"""

from flask import Flask, redirect, url_for

import config

app = Flask(__name__)


@app.route("/")
def base():
    return "", 400


@app.route("/board")
def board():
    return redirect(url_for("static", filename="board.html"))


@app.route("/graphic")
def graphic():
    return redirect(url_for("static", filename="graphic.html"))


@app.route("/control")
def control():
    return redirect(url_for("static", filename="control.html"))


@app.route("/info")
def hashtag():
    return {
        "hashtag": config.HASHTAG,
        "ws_conn": "ws://{0}:{1}".format(config.HOST, config.WS_PORT)
    }


def http_server() -> None:
    print("Starting HTTP Server")
    app.run(host=config.HOST, port=config.PORT, debug=True, use_reloader = False)


if __name__ == "__main__":
    print("Don't do this")
