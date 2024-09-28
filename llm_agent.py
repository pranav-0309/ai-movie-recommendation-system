# All project imports
import pandas as pd
from langchain_groq import ChatGroq
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
import json

# Loading the dataset
movies = pd.read_csv("cleaned_movies.csv")

# Initializing the LLM
llm = ChatGroq(
    temperature=0.5,
    api_key='YOUR_API_KEY', # type: ignore
    model='llama3-70b-8192',
    stop_sequences=None,
    max_tokens=8000
)

# Creating an agent to interact with the dataset
# Note: The query was written in such a format to make sure the LLM does not reach it's max input length limit.
def filter_movies(genres="any", year="any year", original_language="any", adult="False"):
    # Instantiate the agent
    agent = create_pandas_dataframe_agent(llm, 
                                        movies,
                                        verbose=False, 
                                        allow_dangerous_code=True,
                                        handle_parsing_errors=True)
    # Set the query based on user filters
    if genres == "Any" and year == "Any year" and original_language == "Any" and adult == "False":   
        query = "Select up to 5 random movies with 'adult' set to 'False' and return their 'title' and 'poster_path' in a JSON format with no explaination. NO PREAMBLE."
    elif genres == "Any" and year == "Any year" and original_language == "Any" and adult == "True":
        query = "Select up to 5 random movies with 'adult' set to 'True' and return their 'title' and 'poster_path' in a JSON format with no explaination. NO PREAMBLE."
    else:
        query = f"Select up to 5 movies and return their 'title' and 'poster_path' in a JSON format with no preamble where {genres} are in the 'genres', 'release_year' is between {year}, 'original_language' is {original_language} and 'adult' is set to {adult}. If no movies were found return 'No movies found.' only and nothing else."
    result = agent.run(query)
    return result

def extract_movie_info(json_result):
    try:
        if json_result == "No movies found.":
            return [], []
        # Parse the JSON string
        movies_data = json.loads(json_result)
        # Initialize empty lists for titles and poster paths
        titles = []
        poster_paths = [] 
        # Extract titles and poster paths
        for movie in movies_data:
            if isinstance(movie, dict):
                titles.append(movie.get('title', ''))
                # Remove leading '\' if present
                poster_path = movie.get('poster_path', '')
                if poster_path.startswith('\\'):
                    poster_path = poster_path[1:]
                poster_paths.append(poster_path)
        return titles, poster_paths
    except json.JSONDecodeError:
        return [], []
    except KeyError as e:
        return [], []