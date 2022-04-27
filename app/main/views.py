'''
We define views that will be rendered on our pages

# Views
@main.route('/')  #route decorator
def index(): #view function
   # Getting popular movie
   popular_movies = get_movies('popular')
   upcoming_movie = get_movies('upcoming')
   now_showing_movie = get_movies('now_playing')
   title = 'Home - Welcome to The best Movie Review Website Online'

   search_movie = request.args.get('movie_query')

   if search_movie:
      return redirect(url_for('.search',movie_name=search_movie))
  
   return render_template('index.html', title = title, popular = popular_movies, upcoming = upcoming_movie, now_showing = now_showing_movie )
'''
from multiprocessing import context
from flask import render_template,request,redirect,url_for
from . import main
from app.request import *
from app.models import Books

#Views
@main.route('/')
def index():
   flask_books = get_books('flask')
   python_books = get_books('python')
   django_books = get_books('django')
   
   return render_template('index.html',flask_books=flask_books,python_books=python_books,django_books=django_books)