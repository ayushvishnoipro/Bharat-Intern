import pickle
import streamlit as st
import requests


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie = []
    recommended_movie_poster = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        # recommended_movie_poster.append(fetch_poster(movie_id))
        recommended_movie.append(movies.iloc[i[0]].title)

    return recommended_movie 


# , recommended_movie_posters


st.header('Movie Recommender System')
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown", movie_list
)
if st.button('Show Recommendation'):
    recommended_movie_names = recommend(selected_movie)
    for i in recommended_movie_names:
        st.write(i)
    # col1, col2, col3, col4, col5 = st.beta_columns(5)
