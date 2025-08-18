from datetime import datetime, date
from sqlalchemy.orm import validates
from sqlalchemy import func
from . import db

class Episode(db.Model):
    __tablename__ = "episodes"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, default=lambda: datetime.today().date(), server_default=func.current_date(), nullable=False)
    number = db.Column(db.Integer, nullable=False)

    appearances = db.relationship(
        "Appearance", back_populates="episode", cascade="all, delete-orphan"
    )
    
    def to_dict_episodes(self):
        return {
            "id": self.id,
            "date": self.date.strftime("%d/%m/%Y"),
            "number": self.number
        }
    
    def to_dict_episode(self):
        return {
            "id": self.id,
            "date": self.date.strftime("%d/%m/%Y"),
            "number": self.number,
            "appearances": [
                {
                    "id": a.id,
                    "episode_id": a.episode_id,
                    "rating": a.rating,
                    "guest": {
                        "id": a.guest.id,
                        "name": a.guest.name,
                        "occupation": a.guest.occupation
                    }
                } for a in self.appearances #type: ignore
            ]
        }

    @validates("date")
    def validate_date(self, key, value):
        if isinstance(value, str):
            try:
                parsed_date = datetime.strptime(value.strip(), "%d/%m/%Y").date()
            except ValueError:
                raise ValueError("Invalid date. Use dd/mm/yyyy format.")
        elif isinstance(value, datetime):
            parsed_date = value.date()
        elif isinstance(value, date):
            parsed_date = value
        elif value is None:
            raise ValueError("Date cannot be empty.")
        else:
            raise ValueError(
                "Invalid date. Date must be a string in dd/mm/yyyy format, a datetime object, or a date object."
            )

        if parsed_date.year < 1962:
            raise ValueError(
                "Date is way too far in the past. The earliest 'late show' was an Irish talk show called The Late Late Show, and it aired in 1962."
            )
        if parsed_date > datetime.today().date():
            raise ValueError(
                "Episode must have aired already, so no future dates allowed."
            )
        return parsed_date

    @validates("number")
    def validate_number(self, key, value):
        if isinstance(value, str):
            value = value.strip()

            if not value.isdigit():
                raise ValueError("The episode number must be a positive integer.")
            value = int(value)
        
        if not isinstance(value, int):
            raise ValueError("The episode number must be an integer.")

        if value <= 0:
            raise ValueError("The episode number must be positive.")
        return value
