![ai_movie_pic.jpeg](ai_movie_pic.jpeg)

# AI Movie Recommendation System 🤖🎬

Welcome to the AI Movie Recommendation System, an intelligent solution that uses Large Language Models (LLMs) to provide personalized movie suggestions based on user preferences. This project showcases the integration of an AI agent and a rich dataset to deliver customized recommendations.

## 📽️ Project Overview

This project leverages a 1M+ movie dataset from The Movie Database (TMDB) taken from Kaggle and utilizes an AI Agent powered by Llama3 70B model via an API from Groq. It allows users to filter movies based on several attributes and receive up to 5 personalized recommendations, complete with movie posters.

## 💡 Key Features

- Cleaned and Preprocessed Dataset: Worked with a Kaggle dataset consisting of over 1 million movie entries, cleaning and preprocessing the data to make it ready for querying

- LLM Integration:
  - Integrated Groq's API using the Llama3 70B model to generate personalized movie recommendations based on user-selected filters such as:
    - Genre
    - Original Language
    - Release Year
    - Adult Content Prefernece

- Tech Stack:
  - Python: Programming Language
  - Pandas: For Data Manipulation 
  - LangChain: For AI Agent and LLM Integration
  - Streamlit: Used to create User-Friendly UI

- UI: The Streamlit-based interface allows users to filter movies with ease and retrieve up to 5 personalized recommendations, including movie titles and their corresponding posters

## Project File Structure:

- `ai_movie_test.ipynb` contains the data cleaning code and some testing for the AI Agent
- `llm_agent.py` contains the code for the AI Agent
- `app.py` contains the code for the Streamlit UI
- Please note that you will need to visit https://console.groq.com/playground and create an account and then create an API key for this project
- You will also need to visit https://www.kaggle.com/datasets/asaniczka/tmdb-movies-dataset-2023-930k-movies to download the original dataset and make your own file called `cleaned_movies.csv` as I wasn't able to upload it due to file size limits in GitHub

### Note:

The AI Agent takes several minutes to get the result probably due to the large amount of data and also due to how specific the filters are, hence the genre selection has been limited to a maximum of 5 only and in cases that the AI Agent retrieves less than 5 movies, whatever was retrieved will be shown. If the AI Agent wasn't able to find any movies it return nothing and the user will receive a message saying "No movies found. Please try again with different filters.".
