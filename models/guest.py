from datetime import datetime, date
from sqlalchemy.orm import validates
from sqlalchemy import UniqueConstraint, text, func
from . import db

class Guest(db.Model):
    __tablename__ = "guests"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    occupation = db.Column(db.String(500), nullable=False)

    appearances = db.relationship(
        "Appearance", back_populates="guest", cascade="all, delete-orphan"
    )

    @validates("name")
    def validate_name(self, key, value):
        value = value.strip()

        if not value:
            raise ValueError("Guest name cannot be empty.")
        if len(value) > 200:
            raise ValueError("Guest name is too long.")

        return value

    @validates("occupation")
    def validate_occupation(self, key, value):
        value = value.strip()

        if not value:
            raise ValueError("Guest occupation cannot be empty.")
        if len(value) > 500:
            raise ValueError("Guest occupation is too long.")

        return value
    
    def to_dict_guests(self):
        return {
            "id": self.id,
            "name": self.name,
            "occupation": self.occupation
        }
        
    def to_dict_guest(self):
        return {
            "id": self.id,
            "name": self.name,
            "occupation": self.occupation,
            "appearances": [
                {
                    "id": a.id,
                    "episode_id": a.episode_id,
                    "rating": a.rating,
                    "episode": {
                        "id": a.episode.id,
                        "number": a.episode.number,
                        "date": a.episode.date
                    }
                } for a in self.appearances #type: ignore
            ]
        }
