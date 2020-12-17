import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Movie, Actor


# ASSISTANT_TOKEN = os.getenv('ASSISTANT_TOKEN')
# DIRECTOR_TOKEN = os.getenv('DIRECTOR_TOKEN')

# assistant_auth_header = {'Authorization': f'Bearer {ASSISTANT_TOKEN}'}
# director_auth_heade= {'Authorization': f'Bearer {DIRECTOR_TOKEN}'}


class CapstoneTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = os.environ['TEST_DATABASE_URL']
        setup_db(self.app, self.database_path)
        self.casting_assistant = os.getenv('ASSISTANT_TOKEN')
        self.casting_director = os.getenv('DIRECTOR_TOKEN')

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            # self.db.drop_all()
            self.db.create_all()

            self.new_movie = {
                'title': 'joker',
                'release_year': 2019
            }
            self.new_actor = {
                'name': 'Ryan Gosling',
                'age': 40,
                'gender': 'M',
                'movie_id': 1
            }
            self.update_movie = {
                'title': 'seven',
            }
            self.update_actor = {
                'name': 'Ryan Gosling',
            }

            self.assistant_auth_header = {"Authorization":
                                          "Bearer {}".format
                                          (self.casting_assistant)}
            self.director_auth_header = {"Authorization":
                                         "Bearer {}".format
                                         (self.casting_director)}

    def tearDown(self):
        """Executed after reach test"""
        pass

    # --------Tests for /movies GET as assistant -------- #

    def test_get_all_movies_assistant(self):
        res = self.client().get('/movies', headers=self.assistant_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['movies']))

    def test_401_get_movies_unauthorized_assistant(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_404_get_movies_Not_found_assistant(self):
        res = self.client().get('/moviees', headers=self.assistant_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')

    # --------Tests for /movies GET as director--------#

    def test_get_all_movies_director(self):
        res = self.client().get('/movies',  headers=self.director_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['movies']))

    def test_401_get_movies_unauthorized_director(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_404_get_movies_Not_found_director(self):
        res = self.client().get('/moviees', headers=self.director_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')

    # # --------Tests for /actors GET as assistant --------#

    def test_get_all_actors_assistant(self):
        res = self.client().get('/actors', headers=self.assistant_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actors']))

    def test_401_get_actors_unauthorized_assistant(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_404_get_actors_Not_found_assistant(self):
        res = self.client().get('/actoors', headers=self.assistant_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')

    # # --------Tests for /actors GET as director--------#

    def test_get_all_actors_director(self):
        res = self.client().get('/actors', headers=self.director_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    def test_401_get_actors_unauthorized_director(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_404_get_actors_Not_found_director(self):
        res = self.client().get('/actorrs',  headers=self.director_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')

    # # --------Tests for /movies POST as director--------#

    def test_create_movies_director(self):
        res = self.client().post('/movies', json=self.new_movie,
                                 headers=self.director_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(len(data['movie']))

    def test_401_create_movie_unauthorized_director(self):
        res = self.client().post('/movies', json=self.new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_404_create_movie_Not_found_director(self):
        res = self.client().post('/movvies',
                                 json=self.new_movie,
                                 headers=self.director_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')

    # # --------Tests for /actors POST as director--------#

    def test_create_actors_director(self):
        res = self.client().post('/actors',
                                 json=self.new_actor,
                                 headers=self.director_auth_header)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(len(data['actors']))

    def test_401_create_actor_unauthorized_director(self):
        res = self.client().post('/actors', json=self.new_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_404_create_actors_Not_found_director(self):
        res = self.client().post('/actorrs',
                                 json=self.new_actor,
                                 headers=self.director_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')

    # # --------Tests for /movies PATCH as director--------#

    def test_update_movies_director(self):
        res = self.client().patch('/movies/1',
                                  json=self.update_movie,
                                  headers=self.director_auth_header)
        data = json.loads(res.data)

        movies = Movie.query.filter(Movie.id == 1).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['updated'], 1)
        self.assertTrue(len(data['movie']))

    def test_401_update_movies_unauthorized_director(self):
        res = self.client().patch('/movies/1', json=self.update_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_404_update_movies_not_found_director(self):
        res = self.client().patch('/moviees/1',
                                  json=self.update_movie,
                                  headers=self.director_auth_header)
        data = json.loads(res.data)

        movies = Movie.query.filter(Movie.id == 1).one_or_none()

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')

    # # --------Tests for /actors PATCH as director--------#

    def test_update_actors_director(self):
        res = self.client().patch('/actors/2',
                                  json=self.update_actor,
                                  headers=self.director_auth_header)
        data = json.loads(res.data)

        actors = Actor.query.filter(Actor.id == 2).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['updated'], 2)
        self.assertTrue(len(data['actors']))

    def test_401_update_actors_unauthorized_director(self):
        res = self.client().patch('/actors/2', json=self.update_actor)
        data = json.loads(res.data)

        actors = Actor.query.filter(Actor.id == 2).one_or_none()

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_404_update_actors_not_found_director(self):
        res = self.client().patch('/actorrss/2',
                                  json=self.update_actor,
                                  headers=self.director_auth_header)
        data = json.loads(res.data)

        actors = Actor.query.filter(Actor.id == 2).one_or_none()

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')

    # # --------Tests for /movies delete as director--------#

    def test_delete_movies_director(self):
        res = self.client().delete('/movies/2',
                                   headers=self.director_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 2)
        self.assertTrue(len(data['movies']))

    def test_401_delete_movies_unauthorized_director(self):
        res = self.client().delete('/movies/2')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_404_delete_movies_not_found_director(self):
        res = self.client().delete('/moviees/2',
                                   headers=self.director_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')

    # # --------Tests for /actors delete as director--------#

    def test_delete_actors_director(self):
        res = self.client().delete('/actors/1',
                                   headers=self.director_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 1)
        self.assertTrue(len(data['actors']))

    def test_401_delete_actors_unauthorized_director(self):
        res = self.client().delete('/actors/1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_404_delete_actors_not_found_director(self):
        res = self.client().delete('/actorrs/1',
                                   headers=self.director_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
