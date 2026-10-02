import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Load movie dataset
movies = pd.read_csv("movies.csv")


# Features used for recommendations
features = [
    "genres",
    "keywords",
    "cast",
    "director",
    "overview"
]


# Handle missing values
for feature in features:
    movies[feature] = movies[feature].fillna("")


# Clean additional display fields
movies["release_date"] = movies["release_date"].fillna("")
movies["vote_average"] = movies["vote_average"].fillna(0)
movies["vote_count"] = movies["vote_count"].fillna(0)
movies["runtime"] = movies["runtime"].fillna(0)


# Combine movie features
def combine_features(row):
    return (
        row["genres"] + " "
        + row["keywords"] + " "
        + row["cast"] + " "
        + row["director"] + " "
        + row["overview"]
    )


movies["combined_features"] = movies.apply(
    combine_features,
    axis=1
)


# Convert text into numerical vectors
vectorizer = CountVectorizer(stop_words="english")

count_matrix = vectorizer.fit_transform(
    movies["combined_features"]
)


# Calculate similarity between movies
cosine_sim = cosine_similarity(count_matrix)


def get_movie_index(title):
    """
    Find a movie index using its title.
    """

    matches = movies[
        movies["title"].str.lower() == title.lower()
    ]

    if matches.empty:
        return None

    return matches.index[0]


def recommend_movies(movie_title, num_recommendations=10):
    """
    Return detailed information about similar movies.
    """

    movie_index = get_movie_index(movie_title)

    if movie_index is None:
        return None

    similarity_scores = list(
        enumerate(cosine_sim[movie_index])
    )

    # Sort by similarity
    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    # Remove the selected movie
    top_movies = similarity_scores[
        1:num_recommendations + 1
    ]

    recommendations = []

    for index, score in top_movies:

        movie = movies.iloc[index]

        recommendations.append({
            "title": movie["title"],
            "overview": movie["overview"],
            "genres": movie["genres"],
            "release_date": movie["release_date"],
            "rating": movie["vote_average"],
            "vote_count": movie["vote_count"],
            "runtime": movie["runtime"]
        })

    return recommendations


if __name__ == "__main__":

    recommendations = recommend_movies(
        "moonraker",
        10
    )

    if recommendations:

        print("\nRecommended Movies:\n")

        for movie in recommendations:
            print("-", movie["title"])

    else:
        print("Movie not found.")