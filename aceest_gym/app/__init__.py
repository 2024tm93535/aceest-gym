from flask import Flask
from aceest_gym.app.routes import gym_routes


def create_app():
    app = Flask(__name__)

    # register blueprint
    app.register_blueprint(gym_routes)

    return app