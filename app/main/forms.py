# Create your forms here.
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

class GameForm(FlaskForm):
    body = StringField('Body', validators=[DataRequired(). Length(min=1, max=280)])
    submit = SubmitField('Share')

class ReplyForm(FlaskForm):
    body = StringField('Body', validators=[DataRequired(), Length(min=1, max=280)])
    submit = SubmitField('Reply')