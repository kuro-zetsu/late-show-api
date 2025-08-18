from werkzeug.exceptions import BadRequest, NotFound
from flask import Blueprint, request, jsonify
from models.appearance import Appearance
from models.episode import Episode
from models.guest import Guest
from models import db

episode_bp = Blueprint("episode_bp", __name__, url_prefix="/episodes")


# Get all episodes
@episode_bp.route("/", methods=["GET"])
def get_episodes():
    episodes = Episode.query.all()

    return jsonify([episode.to_dict_episodes() for episode in episodes]), 200


# Get an episode
@episode_bp.route("/<int:episode_id>", methods=["GET"])
def get_episode(episode_id):
    episode = Episode.query.get(episode_id)

    if not episode:
        raise NotFound("Episode not found")

    return jsonify(episode.to_dict_episode()), 200


# Create an episode
@episode_bp.route("/", methods=["POST"])
def create_episode():
    data = request.get_json()

    if not data:
        raise BadRequest("The request body must be JSON.")

    date = data.get("date")
    number = data.get("number")

    if date is None or number is None:
        raise BadRequest("Both 'date' and 'number' are required.")

    try:
        episode = Episode(date=date, number=number)  # type: ignore
    except ValueError as e:
        raise BadRequest(str(e))

    db.session.add(episode)
    db.session.commit()

    return jsonify(episode.to_dict_episode()), 201


# Update an episode
@episode_bp.route("/<int:episode_id>", methods=["PATCH"])
def update_episode(episode_id):
    episode = Episode.query.get(episode_id)

    if not episode:
        raise NotFound("Episode not found")

    data = request.get_json()

    if not data:
        raise BadRequest("The request body must be JSON.")

    if "date" in data:
        try:
            episode.date = data["date"]
        except ValueError as e:
            raise BadRequest(str(e))

    if "number" in data:
        try:
            episode.number = data["number"]
        except ValueError as e:
            raise BadRequest(str(e))

    db.session.commit()

    return jsonify(episode.to_dict_episodes()), 200


# Delete an episode
@episode_bp.route("/<int:episode_id>", methods=["DELETE"])
def delete_episode(episode_id):
    episode = Episode.query.get(episode_id)

    if not episode:
        raise NotFound("Episode not found")

    db.session.delete(episode)
    db.session.commit()

    return "", 204
