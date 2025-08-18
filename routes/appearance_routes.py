from werkzeug.exceptions import BadRequest, NotFound
from flask import Blueprint, request, jsonify
from models.appearance import Appearance
from models.episode import Episode
from models.guest import Guest
from models import db

appearance_bp = Blueprint("appearance_bp", __name__, url_prefix="/appearances")


# Get all appearances
@appearance_bp.route("/", methods=["GET"])
def get_appearances():
    appearances = Appearance.query.all()

    return (
        jsonify([appearance.to_dict_appearances() for appearance in appearances]),
        200,
    )


# Get an appearance
@appearance_bp.route("/<int:appearance_id>", methods=["GET"])
def get_appearance(appearance_id):
    appearance = Appearance.query.get(appearance_id)

    if not appearance:
        raise NotFound("Appearance not found")

    return jsonify(appearance.to_dict_appearance()), 200


# Create an appearance
@appearance_bp.route("/", methods=["POST"])
def create_appearance():
    data = request.get_json()

    if not data:
        raise BadRequest("The request body must be JSON.")

    rating = data.get("rating")
    episode_id = data.get("episode_id")
    guest_id = data.get("guest_id")
    
    errors = []

    if episode_id is None: 
        errors.append("episode_id is required")
    elif not Episode.query.get(episode_id):
        errors.append("Episode not found")
    
    if guest_id is None:
        errors.append("guest_id is required")
    elif not Guest.query.get(guest_id):
        errors.append("Guest not found")

    if rating is not None:
        try:
            Appearance().validate_rating("rating", rating)
        except ValueError as e:
            errors.append(str(e))
    
    if errors:
        return jsonify({"errors": errors}), 400
        
    appearance = Appearance(rating=rating, episode_id=episode_id, guest_id=guest_id)  # type: ignore

    db.session.add(appearance)
    db.session.commit()

    return jsonify(appearance.to_dict_appearance()), 201


# Update an appearance
@appearance_bp.route("/<int:appearance_id>", methods=["PATCH"])
def update_appearance(appearance_id):
    appearance = Appearance.query.get(appearance_id)

    if not appearance:
        raise NotFound("Appearance not found")

    data = request.get_json()
    
    if not data:
        raise BadRequest("The request body must be JSON.")

    if "rating" in data:
        try:
            appearance.rating = data["rating"]
        except ValueError as e:
            raise BadRequest(str(e))

    if "episode_id" in data:
        if not Episode.query.get(data["episode_id"]):
            raise NotFound(f"No episode found with ID {data["episode_id"]}.")
        appearance.episode_id = data["episode_id"]

    if "guest_id" in data:
        if not Guest.query.get(data["guest_id"]):
            raise NotFound(f"No guest found with ID {data["guest_id"]}.")
        appearance.guest_id = data["guest_id"]

    db.session.commit()

    return jsonify(appearance.to_dict_appearances()), 200


# Delete an appearance
@appearance_bp.route("/<int:appearance_id>", methods=["DELETE"])
def delete_appearance(appearance_id):
    appearance = Appearance.query.get(appearance_id)

    if not appearance:
        raise NotFound("Appearance not found")

    db.session.delete(appearance)
    db.session.commit()

    return "", 204
