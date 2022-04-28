'''
We define views that will be rendered on our pages
'''
from multiprocessing import context
from unicodedata import category
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

   search_book = request.args.get('book_query')

   if search_book:
      return redirect(url_for('.search',book=search_book))
   
   return render_template('index.html',flask_books=flask_books,python_books=python_books,django_books=django_books)

@main.route('/search/<book>')
def search(book):
   books_name_list = book.split(" ")
   book_name_format = "+".join(books_name_list)
   searched_books = search_book(book_name_format)
   title = book.capitalize()

   return render_template('search.html', searched_books=searched_books, title=title)

@main.route('/book/<int:id>')
def get_book(id):
   book = get_book(id)

   return render_template('book.html',book=book)