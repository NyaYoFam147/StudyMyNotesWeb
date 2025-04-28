from flask import Flask, render_template, request, redirect
import webbrowser

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        query = request.form["query"]
        return redirect(f"https://www.google.com/search?q={query}")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
