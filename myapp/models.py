#!/usr/bin/env python3

from datetime import datetime
from myapp import db

class Cent(db.Model):
    __tablename__ = 'cents'
    
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, default=1)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)