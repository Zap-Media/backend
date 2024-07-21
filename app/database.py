from pymongo import MongoClient

from uuid import uuid4
import random
from datetime import datetime

from config import Config

class Database:
    def __init__(self) -> None:
        self.conn = MongoClient(Config.MONGO_URL)
        self.db = self.conn['zap']

        self.users = self.db['users']

        self.social_users = self.db['social']

        self.posts = self.db['posts']

    def fetch_user(self, key, value):
        return self.users.find_one({key: value})

    def fetch_sub_user(self, db, key, value):
        return db.find_one({key: value})

    def create_user(self, email):
        name = email.split("@")[0] + "".join([random.randint(0, 9) for _ in range(10)])
        user_obj = {
            "_id": str(uuid4()),
            "username": name,
            "name": name,
            "created": datetime.now().timestamp()
        }
        self.users.insert_one(user_obj)

    def create_social_user(self, user_id):
        user_obj = {
            "_id": str(uuid4()),
            "parent": user_id,
            "bio": "",
            "created": datetime.now().timestamp(),
            "posts": [],
            "history": [],
            "followers": [],
            "following": []
        }
        self.social_users.insert_one(user_obj)