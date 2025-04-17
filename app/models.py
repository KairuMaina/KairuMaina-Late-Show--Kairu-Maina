# app/models.py
from . import db
from sqlalchemy.orm import validates

class Episode(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    date        = db.Column(db.String(100), nullable=False)
    number      = db.Column(db.Integer, nullable=False, unique=True)
    appearances = db.relationship(
        'Appearance', back_populates='episode',
        cascade='all, delete-orphan'
    )

    def to_dict(self):
        return {
            'id': self.id,
            'date': self.date,
            'number': self.number
        }

    def to_dict_with_appearances(self):
        d = self.to_dict()
        d['appearances'] = [
            a.to_dict(include_episode=False, include_guest=True)
            for a in self.appearances
        ]
        return d

class Guest(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    name        = db.Column(db.String(100), nullable=False)
    occupation  = db.Column(db.String(100), nullable=False)
    appearances = db.relationship(
        'Appearance', back_populates='guest',
        cascade='all, delete-orphan'
    )

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'occupation': self.occupation
        }

class Appearance(db.Model):
    id         = db.Column(db.Integer, primary_key=True)
    rating     = db.Column(db.Integer, nullable=False)
    episode_id = db.Column(
        db.Integer, db.ForeignKey('episode.id', ondelete='CASCADE'),
        nullable=False
    )
    guest_id   = db.Column(
        db.Integer, db.ForeignKey('guest.id', ondelete='CASCADE'),
        nullable=False
    )

    episode = db.relationship('Episode', back_populates='appearances')
    guest   = db.relationship('Guest',   back_populates='appearances')

    @validates('rating')
    def validate_rating(self, key, value):
        if not (1 <= value <= 5):
            raise ValueError('rating must be between 1 and 5')
        return value

    def to_dict(self, include_episode=True, include_guest=True):
        data = {
            'id': self.id,
            'rating': self.rating,
            'episode_id': self.episode_id,
            'guest_id': self.guest_id
        }
        if include_episode:
            data['episode'] = self.episode.to_dict()
        if include_guest:
            data['guest']   = self.guest.to_dict()
        return data
