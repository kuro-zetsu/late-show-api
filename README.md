# Late Show API

A lightweight and intuitive **Flask API** that allows management of episodes, guests, and ratings for a fictional late-night talk show. It provides endpoints to create, read, update, and delete entries while enforcing validation rules such as correct date formats and preventing future-dated episodes. **SQLite** is used as the database backend, and **SQLAlchemy ORM** ensures smooth database interactions.

---

### Features

* Manage episodes including their dates and identifiers.
* Manage guests and track their appearances.
* Record and access ratings for episodes.
* Enforces input validation for dates (`dd/mm/yyyy`) and prevents future dates.
* **SQLite** database integration via **SQLAlchemy**.
* Database migrations handled with **Flask-Migrate**.

---

### Tech Stack

* **Python** 3.10+
* **Flask**
* **Flask-SQLAlchemy**
* **Flask-Migrate**
* **SQLite**
* **python-dotenv**

---

### Project Structure

```
    lateshow-reagan-nyauma/
    ├── app.py                # Application entry point
    ├── seed.py               # Script to populate initial data
    ├── Pipfile               # Pipenv dependency definitions
    ├── Pipfile.lock          # Locked dependencies
    ├── README.md             # Project documentation
    ├── .env                  # Environment variables (not tracked in git)
    ├── .gitignore            # Git ignore rules
    ├── instance/
    │   └── lateshow.db       # SQLite database (kept for marking)
    ├── migrations/           # Database migrations
    │   ├── env.py
    │   ├── README
    │   ├── alembic.ini
    │   ├── script.py.mako
    │   └── versions/
    │       └── 02ea614e0c21_initial.py   # Initial migration (kept)
    ├── models/               # Database models
    │   ├── __init__.py
    │   ├── appearance.py
    │   ├── episode.py
    │   └── guest.py
    └── routes/               # API routes
    ├── __init__.py
    ├── appearance_routes.py
    ├── episode_routes.py
    └── guest_routes.py
```
--- 

### Setup Instructions

1.  **Clone the repository**
    ```bash
    git clone https://github.com/Moringa-SDF-PT10/lateshow-reagan-nyauma.git
    cd lateshow-reagan-nyauma
    ```
2.  **Create and activate a virtual environment with pipenv**
    ```bash
    pipenv install
    pipenv shell
    ```
3.  **Configure environment variables**
    Create a `.env` file in the project root with the following contents:
    ```
    SQLALCHEMY_DATABASE_URI=sqlite:///lateshow.db
    SECRET_KEY=your_secret_key_here
    FLASK_APP=app.py
    FLASK_RUN_PORT=5555
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    JSON_SORT_KEYS=False
    ```
4.  **Initialize the database and perform initial migration**
    ```bash
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade
    ```
5.  **Run the server**
    ```bash
    flask run
    ```
    The API will be accessible at `http://127.0.0.1:5555`

---

### API Endpoints

#### Episodes

* `GET /episodes/` - Retrieve all episodes
* `GET /episodes/<episode_id>` - Retrieve a specific episode
* `POST /episodes/` - Create a new episode
* `PATCH /episodes/<episode_id>` - Update an episode
* `DELETE /episodes/<episode_id>` - Delete an episode

#### Guests

* `GET /guests/` - Retrieve all guests
* `GET /guests/<guest_id>` - Retrieve a specific guest
* `POST /guests/` - Create a new guest
* `PATCH /guests/<guest_id>` - Update a guest
* `DELETE /guests/<guest_id>` - Delete a guest

#### Appearances

* `GET /appearances/` - Retrieve all appearances
* `GET /appearances/<appearance_id>` - Retrieve a specific appearance
* `POST /appearances/` - Create a new appearance
* `PATCH /appearances/<appearance_id>` - Update an appearance
* `DELETE /appearances/<appearance_id>` - Delete an appearance

---

### Notes

* All dates must be in `dd/mm/yyyy` format.
* Future dates are not accepted.
* JSON responses preserve the key order as defined in models.