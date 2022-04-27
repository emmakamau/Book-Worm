'''
Where we define our forms e.g

from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import InputRequired

class ReviewForm(FlaskForm):
    title = StringField('Review title',validators=[InputRequired()])
    review = TextAreaField('Movie review', validators=[InputRequired()])
    submit = SubmitField('Submit')

'''