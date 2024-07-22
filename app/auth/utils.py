import jwt

from datetime import datetime
from datetime import timedelta

from config import Config
from app import db

def gen_tokens(user_obj, sub_user, service):
    d = datetime.now()
    access_obj = {
        "_id": user_obj['_id'],
        'sub_user': sub_user['_id'],
        "email": user_obj['email'],
        "service": service,
        "exp": d+timedelta(days=Config.TOKEN_EXP['access'])
    }

    refresh_obj = {
        "_id": user_obj['_id'],
        "service": service,
        "exp": d+timedelta(days=Config.TOKEN_EXP['access'])
    }

    return {
        "success": True,
        "access_token": jwt.encode(access_obj, Config.JWT_SECRET),
        "refresh_token": jwt.encode(refresh_obj, Config.JWT_SECRET),
    }

def regen_tokens(refresh_token):
    try:
        refresh_obj = jwt.decode(refresh_token, Config.JWT_SECRET)
    except jwt.ExpiredSignatureError:
        return {"success": False, "message": "refresh token expired"}
    except Exception as e:
        return {"success": False, "message": e}
    
    _id = refresh_obj['_id']
    service = refresh_obj['service']
    user = db.fetch_user("_id", _id)

    if service == 'zap-social':
        sub_user = db.fetch_sub_user(db.social_users, "parent", _id)

    return gen_tokens(user, sub_user, service)

def validate_access_token(access_token):
    try:
        decoded = jwt.decode(access_token, Config.JWT_SECRET)
    except jwt.ExpiredSignatureError:
        return {"success": False, "message": "access token expired"}
    except Exception as e:
        return {"success": False, "message": e}
    return {"success": True, "obj": decoded}