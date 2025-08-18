from sqlalchemy.orm import validates
from sqlalchemy import UniqueConstraint, text
from . import db

class Appearance(db.Model):
    __tablename__ = "appearances"
    
    __table_args__ = (
        UniqueConstraint("episode_id", "guest_id", name='once_per_episode'),
    )

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, default=3, server_default=text("3"), nullable=False)

    episode_id = db.Column(db.Integer, db.ForeignKey("episodes.id"), nullable=False)
    guest_id = db.Column(db.Integer, db.ForeignKey("guests.id"), nullable=False)

    episode = db.relationship("Episode", back_populates="appearances")
    guest = db.relationship("Guest", back_populates="appearances")
    
    def to_dict_appearances(self):
        return {
            "id": self.id,
            "rating": self.rating,
            "guest_id": self.guest_id,
            "episode_id": self.episode_id
        }
    
    def to_dict_appearance(self):
        return {
            "id": self.id,
            "rating": self.rating,
            "guest_id": self.guest_id,
            "episode_id": self.episode_id,
            "episode": {
                "id": self.episode.id,
                "number": self.episode.number,
                "date": self.episode.date.strftime("%d/%m/%Y")
            },
            "guest": {
                "id": self.guest.id,
                "name": self.guest.name,
                "occupation": self.guest.occupation
            }
        }
    
    @validates("rating")
    def validate_rating(self, key, value):
        if isinstance(value, str):
            value = value.strip()
            
            if not value.isdigit():
                raise ValueError("The rating has to be a whole number between 1 and 5.")
            
            value = int(value)
        
        elif not isinstance(value, int):
            raise ValueError("The rating has to be a whole number between 1 and 5.")
        
        if not 1 <= value <= 5:
            raise ValueError("The rating must be between 1 and 5.")
        
        return value
