import streamlit as st
import pickle
import pandas as pd

movies = pickle.load(open('../models/movies.pkl', 'rb'))
similarity = pickle.load(open('../models/similarity.pkl', 'rb'))

def recommend(movie):

    movie_index = movies[movies['title'] == movie].index[0]

    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []

    for i in movies_list:
        movie_data = movies.iloc[i[0]]
        recommended_movies.append({
            "title": movie_data.title,
            "rating": round(movie_data.user_rating, 1)
        })    

    return recommended_movies


st.title("Movie Recommendation System")

selected_movie = st.selectbox(
    "Select a movie",
    movies['title'].values
)

if st.button("Recommend"):

    recommendations = recommend(selected_movie)

    for movie in recommendations:

        st.write(
            f"🎬 {movie['title']} ⭐ Rating: {movie['rating']}"
        )