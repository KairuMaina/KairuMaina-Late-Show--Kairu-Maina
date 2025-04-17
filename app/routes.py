# app/routes.py
from flask import Blueprint, request, jsonify
from .models import db, Episode, Guest, Appearance

api_bp = Blueprint('api', __name__)

@api_bp.route('/episodes', methods=['GET'])
def get_episodes():
    eps = Episode.query.all()
    return jsonify([e.to_dict() for e in eps]), 200

@api_bp.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    ep = Episode.query.get(id)
    if not ep:
        return jsonify({'error': 'Episode not found'}), 404
    return jsonify(ep.to_dict_with_appearances()), 200

@api_bp.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([g.to_dict() for g in guests]), 200

@api_bp.route('/appearances', methods=['POST'])
def create_appearance():
    data = request.get_json() or {}
    rating     = data.get('rating')
    episode_id = data.get('episode_id')
    guest_id   = data.get('guest_id')

    # existence check
    ep  = Episode.query.get(episode_id)
    gu  = Guest.query.get(guest_id)
    if not ep or not gu:
        return jsonify({'errors': ['Invalid episode_id or guest_id']}), 400

    try:
        ap = Appearance(rating=rating, episode=ep, guest=gu)
        db.session.add(ap)
        db.session.commit()
    except ValueError as ve:
        return jsonify({'errors': [str(ve)]}), 400

    return jsonify(ap.to_dict()), 201
