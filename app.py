import streamlit as st
from llm_agent import movies, filter_movies, extract_movie_info

st.set_page_config(layout="wide")

# Streamlit UI for user input
st.title("🤖 AI Movie Recommendation System")

# Function to limit selections
def limit_selection(selected_genres):
    if len(selected_genres) > 5:
        st.warning("Warning: Only the first 5 genres will be taken.")
        return selected_genres[:5]  # Truncate the selection to the first 5
    return selected_genres

genre_options = [x.strip() for x in "Any, Action, Science Fiction, Adventure, Drama, Crime, Thriller, Fantasy, Comedy, Romance, Western, Mystery, War, Animation, Family, Horror, Music, History, TV Movie, Documentary".split(',')]
language_options = ['Any'] + list(movies['original_language'].unique())
year_options = ['Any year','1960-1970','1980-1990','1990-2000','2000-2010','2010-2020','2020-2024']

# Filters
genres = st.multiselect('Select Genres:', options=genre_options, default='Any')
genres = limit_selection(genres)
language = st.selectbox('Select Language:', options=language_options)
year = st.selectbox('Select Year:', options=year_options)
adult_content = st.selectbox('Adult Content:', options=[False,True])

# Trigger search when the button is clicked
if st.button('SEARCH FOR MOVIES'):
    # Generates the recommendations
    recommendations = filter_movies(genres=str(genres), year=str(year), original_language=str(language), adult=str(adult_content))
    # Extracts the movie titles and poster paths
    titles, poster_paths = extract_movie_info(recommendations)
    # Prints this incase no movies where found
    if not titles or not poster_paths:
        st.write("No movies found. Please try again with different filters.")
    # Displays the titles and posters for less than 5 movies    
    elif len(titles) and len(poster_paths) < 5:
        cols = st.columns(len(titles))
        for i, (title, poster_path) in enumerate(zip(titles, poster_paths)):
            with cols[i % len(titles)]:
                st.text(title)
                st.image("https://image.tmdb.org/t/p/w500" + poster_path)
    # Displays the titles and posters for 5 movies
    else:
        cols = st.columns(5)
        for i, (title, poster_path) in enumerate(zip(titles, poster_paths)):
            with cols[i % 5]:
                st.text(title)
                st.image("https://image.tmdb.org/t/p/w500" + poster_path)
