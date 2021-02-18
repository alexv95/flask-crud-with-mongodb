from flask import Flask, render_template, redirect, request
from flask_material import Material
from business.classes.users import UserDocument

app = Flask(__name__)
Material(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/test", methods=["POST"])
def testForm():
    pass


if __name__ == '__main__':
    app.run(debug=True)
