# 🎬 Movie Recommendation System

A **content-based movie recommendation system** built using Python and Scikit-learn.

The system recommends movies similar to a selected movie by analyzing movie metadata such as **genres, keywords, cast, director, and overview**.

A Flask web application provides a simple interface where users can enter a movie title and receive a list of similar movies.

---

## 🚀 Features

* Content-based movie recommendations
* Movie metadata preprocessing using Pandas
* Text feature extraction using CountVectorizer
* Movie similarity calculation using cosine similarity
* Top 10 similar movie recommendations
* Flask-based web application
* Clean and responsive web interface
* Movie details including:

  * Release year
  * Runtime
  * Rating
  * Genres
  * Overview
* Handles invalid or unavailable movie titles

---

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **Flask**
* **HTML5**
* **CSS3**
* **Jupyter Notebook**

---

## 🧠 How It Works

The recommendation system follows these steps:

1. Load the movie dataset using Pandas.
2. Handle missing values in important movie features.
3. Combine genres, keywords, cast, director, and overview into a single text representation.
4. Convert the combined text into numerical vectors using **CountVectorizer**.
5. Calculate similarity between movies using **Cosine Similarity**.
6. Find the movies with the highest similarity to the selected movie.
7. Display the top 10 recommendations through the Flask web application.

### Recommendation Flow

```text
Movie Dataset
      ↓
Data Preprocessing
      ↓
Feature Combination
      ↓
CountVectorizer
      ↓
Cosine Similarity
      ↓
Similar Movies
      ↓
Flask Web Application
      ↓
User Interface
```

---

## 📂 Project Structure

```text
Movie-Recommendation-System/
│
├── app.py
├── recommendation.py
├── movies.csv
├── movie_recommendation_analysis.ipynb
├── requirements.txt
├── .gitignore
├── README.md
│
├── templates/
│   ├── index.html
│   └── result.html
│
└── static/
    └── style.css
```

> The `.venv` virtual environment is used locally and is excluded from Git using `.gitignore`.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
```

### 2. Open the project folder

```bash
cd Movie-Recommendation-System
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

For Windows PowerShell:

```bash
.\.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Flask application:

```bash
python app.py
```

The application will run locally at:

```text
http://127.0.0.1:5000
```

Open the address in your browser.

---

## 🎯 Example

Enter a movie title such as:

```text
Moonraker
```

The system analyzes the movie's metadata and displays similar movies.

---

## 📊 Model Development

The model development process is documented in:

```text
movie_recommendation_analysis.ipynb
```

The notebook contains the data loading, preprocessing, feature engineering, vectorization, similarity calculation, and recommendation testing steps.

---

## 🔍 Recommendation Approach

This project uses a **content-based filtering approach**.

Instead of using user ratings or user history, the system compares the characteristics of movies.

The main features used are:

* Genres
* Keywords
* Cast
* Director
* Overview

The combined text is transformed into numerical vectors using **CountVectorizer**.

Cosine similarity is then used to determine how similar two movies are.

---

## ⚠️ Limitations

* Recommendations depend on the quality of the movie metadata.
* The system does not use user viewing history.
* It does not implement collaborative filtering.
* Movie posters are not included in the current dataset.
* The system requires the movie title to exist in the dataset.

---

## 🔮 Future Improvements

Possible improvements include:

* Add movie poster integration
* Improve movie title matching
* Add fuzzy search
* Improve recommendation ranking
* Add user-based recommendations
* Deploy the application online
* Add a larger and more regularly updated dataset

---

## 👩‍💻 Author

**Prachi Tundiya**

B.Sc. IT (Honours)
Parul University

GitHub: `prachitundiya`
