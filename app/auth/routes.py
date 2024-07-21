from flask import jsonify, session, redirect, url_for, request, abort, flash
import secrets
from urllib.parse import urlencode
import requests

from app.auth import bp
from config import Config
from app import db

@bp.route('/authorize/<provider>')
def oauth2_authorize(provider):
    provider_data = Config.OAUTH2_PROVIDERS.get(provider)

    session['oauth2_state'] = secrets.token_urlsafe(16)

    redirect_url = request.args.get("redirect")
    if redirect_url not in Config.ALLOWED_REDIRECTS:
        return abort(406)

    qs = urlencode({
        'client_id': provider_data['client_id'],
        'redirect_uri': redirect_url,
        'response_type': 'code',
        'scope': ' '.join(provider_data['scopes']),
        'state': session['oauth2_state'],
    })

    return redirect(provider_data['authorize_url'] + '?' + qs)


@bp.route('/callback/<provider>')
def oauth2_callback(provider):

    provider_data = Config.OAUTH2_PROVIDERS.get(provider)

    if 'error' in request.args:
        for k, v in request.args.items():
            if k.startswith('error'):
                flash(f'{k}: {v}')
        return redirect(url_for('index'))

    if request.args['state'] != session.get('oauth2_state'):
        abort(401)

    if 'code' not in request.args:
        abort(401)

    if request.args.get("service") not in Config.SERVICES:
        abort(406)

    response = requests.post(provider_data['token_url'], data={
        'client_id': provider_data['client_id'],
        'client_secret': provider_data['client_secret'],
        'code': request.args['code'],
        'grant_type': 'authorization_code',
        'redirect_uri': request.args['redirect'],
    }, headers={'Accept': 'application/json'})

    if response.status_code != 200:
        abort(401)
    
    oauth2_token = response.json().get('access_token')

    if not oauth2_token:
        abort(401)

    response = requests.get(provider_data['userinfo']['url'], headers={
        'Authorization': 'Bearer ' + oauth2_token,
        'Accept': 'application/json',
    })
    if response.status_code != 200:
        abort(401)

    email = provider_data['userinfo']['email'](response.json())

    user = db.fetch_user("email", email)
    if user is None:
        user = db.create_user(email)

    if request.args.get("service") == "zap-social":
        sub_user = db.fetch_sub_user(db.social_users, "email", email)
        if sub_user is None:
            sub_user = db.create_social_user(user['_id'])

    return email