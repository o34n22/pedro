#!/usr/bin/env python3

from myapp import app, db

db.create_all(app=app)
app.run(debug=True)