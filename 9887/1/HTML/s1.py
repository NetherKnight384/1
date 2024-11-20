from flask import render_template, Flask, request

app = Flask(__name__)
@app.route("/")
@app.route("/home", methods = ["GET", "POST"])
def input():
    text = request.form.get("text")
    return render_template("s1.html")
if __name__ == "__main__":
    app.run(debug=True)

