from flask import jsonify

from app.auth import bp

@bp.route("/register")
def register():
    return jsonify({})