from flask import Flask, request, jsonify
from flask_migrate import Migrate
from .models import db, Episode, Guest, Appearance  # Import the models

app = Flask(__name__)

# Configure your app (using SQLite for simplicity)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize the database and migration
db.init_app(app)
migrate = Migrate(app, db)

# Define your routes
@app.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([episode.to_dict() for episode in episodes])

@app.route('/episodes/<int:episode_id>', methods=['GET'])
def get_episode(episode_id):
    episode = Episode.query.get(episode_id)
    if episode:
        return jsonify(episode.to_dict())
    else:
        return jsonify({"message": "Episode not found"}), 404

@app.route('/episodes/<int:episode_id>', methods=['DELETE'])
def delete_episode(episode_id):
    episode = Episode.query.get(episode_id)
    if episode:
        db.session.delete(episode)
        db.session.commit()
        return jsonify({"message": "Episode deleted"}), 200
    else:
        return jsonify({"message": "Episode not found"}), 404

@app.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([guest.to_dict() for guest in guests])

@app.route('/appearances', methods=['POST'])
def create_appearance():
    data = request.get_json()

    # Validate the required fields
    if 'rating' not in data or 'episode_id' not in data or 'guest_id' not in data:
        return jsonify({"errors": ["Missing required fields"]}), 400

    # Ensure rating is between 1 and 5
    if not (1 <= data['rating'] <= 5):
        return jsonify({"errors": ["Rating must be between 1 and 5"]}), 400

    # Create a new appearance
    appearance = Appearance(
        rating=data['rating'],
        episode_id=data['episode_id'],
        guest_id=data['guest_id']
    )
    db.session.add(appearance)
    db.session.commit()

    # Return the newly created appearance with the related episode and guest
    return jsonify(appearance.to_dict(episode=True, guest=True)), 201

# Optional: test route
@app.route('/')
def home():
    return {"message": "App is running!"}

if __name__ == "__main__":
    app.run(debug=True)
