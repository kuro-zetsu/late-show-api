from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
    
from .guest import Guest
from .episode import Episode
from .appearance import Appearance
    