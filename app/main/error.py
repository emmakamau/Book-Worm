'''
from flask import render_template
from . import main

Function to render the 404 error page

@main.app_errorhandler(404)
def four_Ow_four(error):
    
    return render_template('fourOwfour.html'),404
'''