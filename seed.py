from models.appearance import Appearance
from models.episode import Episode
from models.guest import Guest
from sqlalchemy import text
from models import db
from app import app


def seed_episodes():
    episodes = [
    Episode(date="01/01/2025", number=1),
    Episode(date="08/01/2025", number=2),
    Episode(date="15/01/2025", number=3),
    Episode(date="22/01/2025", number=4),
    Episode(date="29/01/2025", number=5),
    ]
    db.session.add_all(episodes)
    db.session.commit()


def seed_guests():
    guests = [
        Guest(name="Alice Johnson", occupation="Comedian"),
        Guest(name="Bob Smith", occupation="Actor"),
        Guest(name="Clara Lee", occupation="Musician"),
        Guest(name="David Kim", occupation="Author"),
        Guest(name="Ella Martinez", occupation="Politician"),
    ]
    db.session.add_all(guests)
    db.session.commit()


def seed_appearances():
    appearances = [
        Appearance(episode_id=1, guest_id=1, rating=5),
        Appearance(episode_id=2, guest_id=2, rating=4),
        Appearance(episode_id=3, guest_id=3, rating=3),
        Appearance(episode_id=4, guest_id=4, rating=5),
        Appearance(episode_id=5, guest_id=5, rating=4),
    ]
    db.session.add_all(appearances)
    db.session.commit()


def clear_tables():
    Appearance.query.delete()
    Episode.query.delete()
    Guest.query.delete()

    try:
        db.session.execute(text("DELETE FROM sqlite_sequence WHERE name='episodes'"))
        db.session.execute(text("DELETE FROM sqlite_sequence WHERE name='guests'"))
        db.session.execute(text("DELETE FROM sqlite_sequence WHERE name='appearances'"))
    except Exception as e:
        print(f"Skipping sequence reset: {e}")

    db.session.commit()


if __name__ == "__main__":
    with app.app_context():
        print("--- Seeding database ---")
        clear_tables()
        seed_episodes()
        seed_guests()
        seed_appearances()
        print("--- Seeding complete! ---")
