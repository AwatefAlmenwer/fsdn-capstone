import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Movie, Actor
from auth import AuthError, requires_auth


def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    # CORS Headers
    @app.after_request
    def after_request(response):
        response.headers.add(
            'Access-Control-Allow-Headers',
            'Content-Type,Authorization,true')
        response.headers.add(
            'Access-Control-Allow-Methods',
            'GET,PUT,POST,DELETE,OPTIONS')
        return response

    @app.route('/')
    def index():
        SECRETS = os.environ.get('SECRETS')
        return 'Welcome to FSND capstone project!!'

    # ---------------------------------------------------------
    # Routes
    # ---------------------------------------------------------

    '''
    GET /movies
    Get list all movies
    '''

    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def get_movies(tokon):
        try:
            movies = list(map(lambda movie: movie.format(), Movie.query.all()))
            return jsonify({
                'success': True,
                'movies': movies
            }), 200
        except:
            abort(404)

    '''
    GET /actors
    Get  list all actors
    '''

    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def get_actors(tokon):
        try:
            actors = list(map(lambda actor: actor.format(), Actor.query.all()))
            return jsonify({
                'success': True,
                'actors': actors
            }), 200
        except:
            abort(404)

    '''
    POST /movies
    Create a new movie
    '''

    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def create_movies(tokon):
        body = request.get_json()
        title = body.get('title', None)
        release_year = body.get('release_year', None)
        try:
            movie = Movie(title=title, release_year=release_year)
            movie.insert()
            return jsonify({
                'success': True,
                'created': [movie.format()]
            }), 200
        except:
            abort(422)

    '''
    POST /actors
    Create new actor
    '''

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def create_actors(tokon):
        body = request.get_json()
        name = body.get('name', None)
        age = body.get('age', None)
        gender = body.get('gender', None)
        movie_id = body.get('movie_id', None)
        try:
            actor = Actor(name=name, age=age, gender=gender, movie_id=movie_id)
            actor.insert()
            return jsonify({
                'success': True,
                'created': [actor.format()]
            }), 200
        except:
            abort(422)

    '''
    PATCH /movies/<id>
    upade the movie where <id> is the existing moive id
    '''
    @app.route('/movies/<int:id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def patch_movie(tokon, id):
        update_movie = Movie.query.filter(Movie.id == id).one_or_none()
        if update_movie:
            try:
                body = request.get_json()
                title = body.get('title', None)
                release_year = body.get('release_year', None)
                if title:
                    update_movie.title = title
                if release_year:
                    update_movie.release_year = release_year
                update_movie.update()
                return jsonify({
                    'success': True,
                    'updated': [update_movie.format()]
                }), 200
            except:
                abort(422)
        else:
            abort(404)

    '''
    PATCH /actors/<id>
    upade the actor where <id> is the existing actor id
    '''

    @app.route('/actors/<int:id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def patch_actor(tokon, id):
        update_actor = Actor.query.filter(Actor.id == id).one_or_none()
        if update_actor:
            try:
                body = request.get_json()
                name = body.get('name', None)
                age = body.get('age', None)
                gender = body.get('gender', None)
                movie_id = body.get('movie_id', None)
                if name:
                    update_actor.name = name
                if age:
                    update_actor.age = age
                if gender:
                    update_actor.gender = gender
                if movie_id:
                    update_actor.movie_id = movie_id
                update_actor.update()
                return jsonify({
                    'success': True,
                    'updated': [update_actor.format()]
                }), 200
            except:
                abort(422)
        else:
            abort(404)
    '''
    DELETE /movies/<id>
    delete the movie by id
    '''

    @app.route('/movies/<int:id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(token, id):
        movie = Movie.query.get(id)
        if movie:
            try:
                movie.delete()
                return jsonify({
                    'success': True,
                    'deleted': id
                }), 200
            except:
                abort(422)
        else:
            abort(404)

    '''
    DELETE /actors/<id>
    delete the actors by id
    '''

    @app.route('/actors/<int:id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(token, id):
        actor = Actor.query.get(id)
        if actor:
            try:
                actor.delete()
                return jsonify({
                    'success': True,
                    'deleted': id
                }), 200
            except:
                abort(422)
        else:
            abort(404)

    # Error Handling

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Resource not found"
        }), 404

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": "Unauthorized"
        }), 401

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
        }), 400

    @app.errorhandler(AuthError)
    def auth_error(error):
        return jsonify({
            "success": False,
            "error": error.status_code,
            "message": error.error
        }), error.status_code

    return app


app = create_app()

if __name__ == '__main__':
    app.run()
