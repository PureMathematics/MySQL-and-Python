from .db import db

class City(db.Document):
    post_id = db.StringField(required=True, unique=True)
    display_url = db.StringField(required=True, unique=True)
    likes = db.StringField(required=True, unique=False)
    location = db.StringField(required=False, unique=False)
    tags = db.ListField(db.StringField(), required=False)
    caption = db.StringField(required=False, unique=False)
    accessibility_caption = db.ListField(db.StringField(), required=False)
    timestamp = db.StringField(required=True, unique=False)
    username = db.StringField(required=True, unique=False)