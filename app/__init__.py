from flask import Flask, jsonify
from dotenv import load_dotenv

load_dotenv()
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    @app.route('/')
    def home():
        return jsonify({"message": "successful"}), 200

    return app