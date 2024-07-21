from flask import Flask, jsonify
from dotenv import load_dotenv

load_dotenv()
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    @app.route('/')
    def home():
        return jsonify({"message": "successful"}), 200

    return app