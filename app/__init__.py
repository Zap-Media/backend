from flask import Flask, jsonify

from config import Config
from app.database import Database

db = Database()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    @app.route('/')
    def home():
        return jsonify({"message": "successful"}), 200

    return app