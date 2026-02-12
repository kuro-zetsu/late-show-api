# Late Show API

**Late Show API** is a RESTful backend service built with **Flask and SQLAlchemy** that models a simplified production system for a late-night talk show. The API manages **episodes, guests, and appearances,** demonstrating relational data modeling, input validation, and clean REST design.

>This project was built as a backend engineering exercise focused on API design, relational database modeling, and production-style development workflows.

---

### Core Capabilities

- RESTful CRUD operations for:

    - Episodes

    - Guests

    - Appearances

- Relational data modeling using SQLAlchemy ORM

- Input validation and error handling

- Database migrations using Flask-Migrate

- Clean modular architecture for scalability

---

### Technical Highlights

- Designed relational models with one-to-many and many-to-many relationships

- Implemented schema validation and domain constraints (date formats, future date prevention)

- Structured routes using modular blueprints

- Applied database migration workflows for safe schema evolution

- Built clear separation between routing, models, and application setup

---

### Tech Stack

* **Python** 3.10+
* **Flask**
* **Flask-SQLAlchemy**
* **Flask-Migrate**
* **SQLite**
* **python-dotenv**

---

### Architecture Overview

```
models/     → Database models & relationships
routes/     → Modular REST API endpoints
migrations/ → Database schema versioning
app.py      → Application entry point

```
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

### Setup

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
    An `.env.example` file is provided with the required variables.  
    Copy it to create your own `.env` file and update the values as needed:

    ```bash
    cp .env.example .env
    ```
    Then open .env and replace placeholder values (e.g., enter-secret-key-here) with your own.
    ```
    # Database configuration
    SQLALCHEMY_DATABASE_URI=sqlite:///lateshow.db

    # Flask configuration
    FLASK_APP=app.py
    FLASK_RUN_PORT=5555
    SECRET_KEY=your-secret-key-here         #Replace this with a secure key

    # SQLAlchemy settings
    SQLALCHEMY_TRACK_MODIFICATIONS=False

    # JSON settings
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

### Possible Improvements

- Authentication & role-based authorization

- Pagination & filtering

- PostgreSQL production deployment

- Automated test coverage

- API documentation (Swagger / OpenAPI)