import datetime
from flask import url_for
from learnflow import db

class User(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    username = db.StringField(max_length=255, required=True)
    first_name = db.StringField(max_length=255, required=True)
    last_name = db.StringField(max_length=255, required=True)
    hashed_pw = db.StringField(max_length=255, required=True)
    saved_tracks = db.ListField(db.StringField)
    mastered_tracks = db.ListField(db.StringField)
    bio = db.StringField(max_length=1000)
    
    def __unicode__(self):
        return "%s %s" % (self.first_name,self.last_name)

    #meta = {
    #    'allow_inheritance': True,
    #    'indexes': ['-created_at', 'slug'],
    #    'ordering': ['-created_at']
    #}


class Link(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    url = db.StringField(max_length=500, required=True)
    description = db.StringField(max_length=500, required=True)  

class Track(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    title = db.StringField(max_length=255, required=True)
    author = db.ReferenceField(User)
    hours = db.IntField(required=True)
    description = db.StringField(max_length=500, required=True)
    links = db.ListField(db.ReferenceField(Link))
    children_tracks = db.ListField(db.ReferenceField('self'))
    prereq = db.ListField(db.StringField(max_length=255))
    tags = db.ListField(db.StringField(max_length=100))
    completed = db.IntField(required=True)
    not_completed = db.IntField(required=True)

class Comments(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    body = db.StringField(required=True)
    author = db.ReferenceField(User)
    track = db.ReferenceField(Track)
    node = db.ReferenceField(Link)

