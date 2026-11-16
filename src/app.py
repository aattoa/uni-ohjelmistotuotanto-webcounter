import flask
from counter import Counter

app = flask.Flask(__name__)
cnt = Counter()

@app.route("/")
def index():
    return flask.render_template("index.html", value=cnt.value)

@app.route("/reset", methods=["POST"])
def reset():
    cnt.reset()
    return flask.redirect("/")

@app.route("/set", methods=["POST"])
def set():
    cnt.set(flask.request.form.get("new_value", 0, type=int))
    return flask.redirect("/")

@app.route("/increment", methods=["POST"])
def increment():
    cnt.increase()
    return flask.redirect("/")
