import csv
from app import app
from app.models import db, Episode, Guest, Appearance


def seed():
    with app.app_context():
        print("Seeding database...")

        # Clear existing records
        Appearance.query.delete()
        Guest.query.delete()
        Episode.query.delete()

        with open('seed.csv') as file:
            reader = csv.DictReader(file)
            for row in reader:
                episode = Episode.query.filter_by(number=row["episode_number"]).first()
                if not episode:
                    episode = Episode(number=int(row["episode_number"]), date=row["episode_date"])
                    db.session.add(episode)

                guest = Guest.query.filter_by(name=row["guest_name"]).first()
                if not guest:
                    guest = Guest(name=row["guest_name"], occupation=row["guest_occupation"])
                    db.session.add(guest)
                    db.session.flush()  # assign guest.id

                appearance = Appearance(
                    rating=int(row["rating"]),
                    episode=episode,
                    guest=guest
                )
                db.session.add(appearance)

            db.session.commit()
        print("✅ Done seeding!")

if __name__ == "__main__":
    seed()
