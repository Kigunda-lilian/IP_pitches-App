from datetime import datetime
from email.policy import default
from app import db
from datetime import datetime

class Pitches(db.Model):
    id = db.column(db.integer,primary_key=True)
    Pitches = db.column(db.string(),nullable=False)
    upvotes = db.column (db.integer(),default=0, nullable=False)
    downvotes = db.column (db.integer(),default=0, nullable=False)
    created_at = db.column (db.DateTime(),default=datetime,nullable=False)