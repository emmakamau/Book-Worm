'''
We define views that will be rendered on our pages

from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_movies,get_movie,search_movie
from .forms import ReviewForm
from ..models import Review


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