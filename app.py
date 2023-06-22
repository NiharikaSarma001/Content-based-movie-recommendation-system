from flask import Flask, render_template, request, url_for
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import linear_kernel
from sklearn.metrics.pairwise import cosine_similarity
from ast import literal_eval

# Load the dataset
path = "D:\morec\dataset"
credits_df = pd.read_csv(path + "/tmdb_5000_credits.csv")
movies_df = pd.read_csv(path + "/tmdb_5000_movies.csv")

# Rename the columns in the credits dataset
credits_df.columns = ['id', 'tittle', 'cast', 'crew']
movies_df = movies_df.merge(credits_df, on="id")

# Demographic Filtering
C = movies_df["vote_average"].mean()
m = movies_df["vote_count"].quantile(0.9)
new_movies_df = movies_df.copy().loc[movies_df["vote_count"] >= m]

def weighted_rating(x, C=C, m=m):
    v = x["vote_count"]
    R = x["vote_average"]
    return (v/(v + m) * R) + (m/(v + m) * C)

new_movies_df["score"] = new_movies_df.apply(weighted_rating, axis=1)
new_movies_df = new_movies_df.sort_values('score', ascending=False)

# Content-Based Filtering
tfidf = TfidfVectorizer(stop_words="english")
movies_df["overview"] = movies_df["overview"].fillna("")
tfidf_matrix = tfidf.fit_transform(movies_df["overview"])

cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
indices = pd.Series(movies_df.index, index=movies_df["title"]).drop_duplicates()




def get_recommendations(title, cosine_sim=cosine_sim):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]

    movies_indices = [ind[0] for ind in sim_scores]
    movies = movies_df["title"].iloc[movies_indices]
    return movies

# Create the Flask app
app = Flask(__name__)

@app.route('/')
def home():
    # return render_template('index.html')
    return render_template('index.html', css=url_for('static', filename='css/styles.css'))

@app.route('/recommend', methods=['POST'])
def recommend():
    title = request.form['title']

    # Call the get_recommendations function to get movie recommendations
    recommendations = get_recommendations(title)

    return render_template('results.html', css=url_for('static', filename='css/results.css'), title=title, recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
