# Create your forms here.
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError, url

class GameForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=5, max=30)])
    body = StringField('Body', validators=[DataRequired(), Length(min=1, max=280)])
    image = StringField('Image', validators=[DataRequired(), url()])
    submit = SubmitField('Share')

class ReplyForm(FlaskForm):
    body = StringField('Body', validators=[DataRequired(), Length(min=1, max=280)])
    submit = SubmitField('Reply')