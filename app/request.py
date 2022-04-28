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
key = None
# Getting the movie base url
base_url = None

def configure_request(app):
    global key,base_url
    key = app.config['BOOKS_API_KEY']
    base_url = app.config['BOOKS_API_BASE_URL']
    print(key)

def get_books(category):
    get_books_url = base_url.format(category,key)
    print(get_books_url)
    with urllib.request.urlopen(get_books_url) as url:
        get_books_data = url.read()
        get_books_response = json.loads(get_books_data)

        books_results = None

        if get_books_response['items']:
            books_results_list = get_books_response['items']
            books_results = process_results(books_results_list)

    return books_results

def process_results(books_list):
    books_results = []
    for books in books_list:
        
        id = books.get('id')
        title = books.get('volumeInfo',{}).get('title')
        authors = books.get('volumeInfo',{}).get('authors')
        publishedDate = books.get('volumeInfo',{}).get('publishedDate')
        description = books.get('volumeInfo',{}).get('description')
        language = books.get('volumeInfo',{}).get('language')
        image = books.get('volumeInfo',{}).get('imageLinks',{}).get('thumbnail')

        books_object = Books(id,title,authors,publishedDate,description,language,image)
        books_results.append(books_object)

    return books_results

def search_book(book):
    search_book_url = 'https://www.googleapis.com/books/v1/volumes?q={}'.format(book)
    with urllib.request.urlopen(search_book_url) as url:
        search_book_data = url.read()
        search_book_response = json.loads(search_book_data)

        search_book_results = None

        if search_book_response['items']:
            search_book_list = search_book_response['items']
            search_book_results = process_results(search_book_list)
    return search_book_results