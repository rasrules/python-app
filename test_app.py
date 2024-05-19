# Importa la clase Flask y la función render_template desde el módulo flask.
from flask import Flask
import unittest
from flask_unittest import ClientTestCase
from app import app

# Crea una instancia de la clase Flask y asigna la aplicación actual a la variable 'app'.
#app = Flask(__name__)

class TestApp(ClientTestCase):
    # Assign the Flask app object
    app = app

    def test_pong_with_client(self, client):
        # Make a request to a route returning "hello world"
        rv = client.get('/ping')
        self.assertResponseEqual(rv, b"pong")


if __name__ == '__main__':
    unittest.main()
