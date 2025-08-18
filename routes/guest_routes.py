from werkzeug.exceptions import BadRequest, NotFound
from flask import Blueprint, request, jsonify
from models.appearance import Appearance
from models.episode import Episode
from models.guest import Guest
from models import db

guest_bp = Blueprint("guest_bp", __name__, url_prefix="/guests")


# Get all guests
@guest_bp.route("/", methods=["GET"])
def get_guests():
    guests = Guest.query.all()

    return jsonify([guest.to_dict_guests() for guest in guests]), 200


# Get a guest
@guest_bp.route("/<int:guest_id>", methods=["GET"])
def get_guest(guest_id):
    guest = Guest.query.get(guest_id)

    if not guest:
        raise NotFound("Guest not found")

    return jsonify(guest.to_dict_guest()), 200


# Create a guest
@guest_bp.route("/", methods=["POST"])
def create_guest():
    data = request.get_json()

    if not data:
        raise BadRequest("The request body has to be JSON.")

    name = data.get("name")
    occupation = data.get("occupation")

    if not name or not occupation:
        raise BadRequest("Both 'name' and 'occupation' are required.")

    try:
        guest = Guest(name=name, occupation=occupation)  # type: ignore
    except ValueError as e:
        raise BadRequest(str(e))

    db.session.add(guest)
    db.session.commit()

    return jsonify(guest.to_dict_guest()), 201


# Update a guest
@guest_bp.route("/<int:guest_id>", methods=["PATCH"])
def update_guest(guest_id):
    guest = Guest.query.get(guest_id)

    if not guest:
        raise NotFound("Guest not found")

    data = request.get_json()

    if not data:
        raise BadRequest("The request body has to be JSON.")

    if "name" in data:
        try:
            guest.name = data["name"]
        except ValueError as e:
            raise BadRequest(str(e))

    if "occupation" in data:
        try:
            guest.occupation = data["occupation"]
        except ValueError as e:
            raise BadRequest(str(e))

    db.session.commit()

    return jsonify(guest.to_dict_guests()), 200


# Delete a guest
@guest_bp.route("/<int:guest_id>", methods=["DELETE"])
def delete_guest(guest_id):
    guest = Guest.query.get(guest_id)

    if not guest:
        raise NotFound("Guest not found")

    db.session.delete(guest)
    db.session.commit()

    return "", 204
