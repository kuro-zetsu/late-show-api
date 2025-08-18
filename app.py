from flask.json.provider import DefaultJSONProvider
from werkzeug.exceptions import HTTPException
from routes import register_routes
from flask_migrate import Migrate
from flask import Flask, jsonify
from dotenv import load_dotenv
from models import db
import os

load_dotenv()


# Custom JSON provider so the keys in responses stop reordering alphabetically
class CustomJSONProvider(DefaultJSONProvider):
    def dumps(self, obj, **kwargs):
        kwargs.setdefault("sort_keys", False)
        return super().dumps(obj, **kwargs)


app = Flask(__name__)
app.json = CustomJSONProvider(app)

migrate = Migrate(app, db)


app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
    "SQLALCHEMY_DATABASE_URI", "sqlite:///lateshow.db"
)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "super-secret-key")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = os.getenv(
    "SQLALCHEMY_TRACK_MODIFICATIONS", "False"
).lower() in ("true", "1", "yes")

db.init_app(app)
register_routes(app)


@app.errorhandler(HTTPException)
def handle_http_exception(e):
    return jsonify({"error": e.description}), e.code
