import os
import sqlite3
from flask import Flask, g, jsonify, request

app = Flask(__name__)

# Database Connection Management

DATABASE = "bacon.db"


def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


# Database Access Functions


def search_actors_by_name(db_cursor, name):
    result = db_cursor.execute("SELECT id FROM actors WHERE name = ?", (name,))
    return [x[0] for x in result.fetchall()]


def get_movies_by_actor(db_cursor, actor_id):
    result = db_cursor.execute(
        """
        SELECT m.title
        FROM movies m, movie_actors ma
        WHERE m.id = ma.movie_id AND ma.actor_id = ?
        """,
        (actor_id,),
    )
    return [x[0] for x in result.fetchall()]


def get_actor_bacon_degree(db_cursor, actor_id):
    result = db_cursor.execute(
        "SELECT degree FROM bacon_degree WHERE id = ?", (actor_id,)
    )
    row = result.fetchone()
    if row is None:
        return row
    return row[0]


# Routes


@app.route("/actors/search/bacon-degree")
def _search_bacon_degree_by_name():
    name = request.args.get("name", None)
    if not name:
        return "Bad Request", 400
    db_cursor = get_db().cursor()
    actor_ids = search_actors_by_name(db_cursor, name)
    return jsonify(
        {
            "actors": [
                {
                    "name": name,
                    "id": actor_id,
                    "movies": [
                        movie for movie in get_movies_by_actor(db_cursor, actor_id)
                    ],
                }
                for actor_id in actor_ids
            ]
        }
    )


@app.route("/actors/search")
def _search_actors_by_name():
    name = request.args.get("name", None)
    if not name:
        return "Bad Request", 400
    db_cursor = get_db().cursor()
    actors = search_actors_by_name(db_cursor, name)
    return jsonify({"actors": actors})


@app.route("/actors/<actor_id>/movies")
def _get_actor_movies(actor_id):
    db_cursor = get_db().cursor()
    movies = get_movies_by_actor(db_cursor, actor_id)
    return jsonify({"movies": movies})


@app.route("/actors/<actor_id>/bacon-degree")
def _get_actor_bacon_degree(actor_id):
    db_cursor = get_db().cursor()
    bacon_degree = get_actor_bacon_degree(db_cursor, actor_id)
    return jsonify({"bacon_degree": bacon_degree})
