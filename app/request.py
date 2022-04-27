'''
Where we request data from the API e.g

def get_movies(category):
    get_movies_url = base_url.format(category,api_key)
    with urllib.request.urlopen(get_movies_url) as url:
        get_movies_data = url.read()
        get_movies_response = json.loads(get_movies_data)

        movie_results = None

        if get_movies_response['results']:
            movie_results_list = get_movies_response['results']
            movie_results = process_results(movie_results_list)

    return movie_results
'''

import urllib.request,json
from .models import Books

# Getting api key
api_key = None
# Getting the movie base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['BOOKS_API_KEY']
    base_url = app.config['BOOKS_API_BASE_URL']