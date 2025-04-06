from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Episode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(500))

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
        }

class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
        }

class Appearance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    episode_id = db.Column(db.Integer, db.ForeignKey('episode.id', ondelete='CASCADE'), nullable=False)
    guest_id = db.Column(db.Integer, db.ForeignKey('guest.id', ondelete='CASCADE'), nullable=False)

    episode = db.relationship('Episode', backref=db.backref('appearances', lazy=True, passive_deletes=True))
    guest = db.relationship('Guest', backref=db.backref('appearances', lazy=True, passive_deletes=True))

    def to_dict(self, episode=False, guest=False):
        data = {
            'id': self.id,
            'rating': self.rating,
        }
        if episode and self.episode:
            data['episode'] = self.episode.to_dict()
        if guest and self.guest:
            data['guest'] = self.guest.to_dict()
        return data
