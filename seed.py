# seed.py
import click, csv
from flask.cli import with_appcontext
from app import create_app, db
from app.models import Episode, Guest, Appearance

@click.command('seed')
@with_appcontext
def seed():
    """Seed the database from seed.csv."""
    db.drop_all()
    db.create_all()

    with open('seed.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # episodes
            ep = Episode.query.filter_by(number=int(row['episode_number'])).first()
            if not ep:
                ep = Episode(number=int(row['episode_number']), date=row['episode_date'])
                db.session.add(ep)

            # guests
            gu = Guest.query.filter_by(name=row['guest_name']).first()
            if not gu:
                gu = Guest(name=row['guest_name'], occupation=row['guest_occupation'])
                db.session.add(gu)
                db.session.flush()

            # appearance
            ap = Appearance(rating=int(row['rating']), episode=ep, guest=gu)
            db.session.add(ap)

        db.session.commit()
    click.echo('✅ Seeded!')

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        seed()
