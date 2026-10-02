from flask import Flask, render_template, request
from recommendation import recommend_movies


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/recommend", methods=["GET", "POST"])
def recommend():

    movie_title = request.form.get("title", "").strip()

    if not movie_title:
        return render_template(
            "result.html",
            movie="",
            recommendations=["Please enter a movie title."]
        )

    recommendations = recommend_movies(movie_title, 10)

    if recommendations is None:
        recommendations = ["Movie not found in dataset."]

    return render_template(
        "result.html",
        movie=movie_title,
        recommendations=recommendations
    )


if __name__ == "__main__":
    app.run(debug=True)