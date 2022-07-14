from flask import Flask, request, url_for, redirect, render_template, jsonify
import anime

# Initalise the Flask app
app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
    # html -> python
    similar_shows = []
    if request.method == "POST":
        anime_name = request.form["anime_show"]
        print(f"{anime_name}")
        similar_shows = anime.get_similar_items(anime_name)
    return render_template("index.html", shows=similar_shows)


@app.route("/similar-item", methods=["POST"])
def similar_items():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
