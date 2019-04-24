from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/add")
def about():
    return render_template("add.html")

@app.route("/archive")
def archive():
    return render_template("archive.html")

if __name__ == "__main__":
    app.run(debug=True)