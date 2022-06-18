from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class SampleForm(FlaskForm):
    userName = StringField('Your name', validators=[DataRequired(), Length(min=1, max=80)])

    submit = SubmitField('Submit')