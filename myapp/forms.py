#!/usr/bin/env python3

from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired

class IntForm(FlaskForm):
    answer = IntegerField('Answer:', validators=[DataRequired()], \
                        render_kw={'autofocus':True})
    submit = SubmitField('Submit')