from flask import Flask
from routes import gym_routes

def create_app():

    app = Flask(__name__)

    app.register_blueprint(gym_routes)

    @app.route("/")
    def home():
        return {"message": "ACEest Gym DevOps API running"}

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)