from .appearance_routes import appearance_bp
from .episode_routes import episode_bp
from .guest_routes import guest_bp
from flask import Flask


def register_routes(app: Flask):
    app.register_blueprint(appearance_bp)
    app.register_blueprint(episode_bp)
    app.register_blueprint(guest_bp)
