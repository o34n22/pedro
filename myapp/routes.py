#!/usr/bin/env python3
"""
doesn't from myapp ... again execute __init__.py inside myapp
and thus instantiate a new object app = Flask(__name__)?

can't I get rid of all the myapp. paths?
"""
from flask import redirect, url_for,\
                  render_template, flash, session
from myapp import app, db
from myapp.forms import IntForm
from myapp.models import Cent
import myapp.mathplay as mp

@app.route('/page1',methods=['GET','POST'])
def page1():
#    answer = None
    num = session.get('number')
    if num is None:
        session['number'] = mp.pose()
    form = IntForm()
    if form.validate_on_submit():
        session['answer'] = form.answer.data # overwrite any existing answer
        if form.answer.data == int(mp.solve(num)): # answer correct
            cent = Cent()
            db.session.add(cent)
            db.session.commit()
            session['number'] = None
        else:
            flash(mp.wrong(num,form.answer.data))
        return redirect(url_for('page1'))
    return render_template('page1.html', form=form,\
                           number=session.get('number'), answer=session.get('answer'))