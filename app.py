import pickle
import streamlit as st 
import requests


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/discover/movie/{}api_key=b56fd3c31c5cebd25ad6b3a415b4f4d0".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "http://image.tmdb.org/t/p/w500/your_poster_path" + poster_path
    
    return full_path


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True , key = lambda x: x[1])
    recommend_movies_name = []
    recommend_movies_poster = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]]['movie_id']
        #recommend_movies_poster.append(fetch_poster(movie_id))
        recommend_movies_name.append(movies.iloc[i[0]].title)
    return recommend_movies_name, recommend_movies_poster 

st.header("Movie Recommendation System Using Machine Learning")
with open('artifacts/movies_list.pkl', 'rb') as file:
    movies = pickle.load(file)
similarity = pickle.load(open('artifacts/similarity.pkl','rb'))


movie_list = movies['title'].values
selected_movie = st.selectbox(
    'Type or select a movie to get recommendation',
    movie_list
)

if st.button('Show recommendation'):
    recommend_movies_name, recommend_movies_poster = recommend(selected_movie)
    st.text(recommend_movies_name[0])
    # st.image(recommend_movies_poster[0])
    
    st.text(recommend_movies_name[1])
    #  st.image(recommend_movies_poster[1])
    
    st.text(recommend_movies_name[2])
    # st.image(recommend_movies_poster[2])
        
   
    st.text(recommend_movies_name[3])
    # st.image(recommend_movies_poster[3])
 
    st.text(recommend_movies_name[4])
    #st.image(recommend_movies_poster[4])