from pymongo import MongoClient
from mafiagg.user import GetUser
from app.utils.database import uri


class UserCollection:
    def __init__(self):
        self.client = MongoClient(uri)
        self.db = self.client["mafiagg"]
        self.user_collection = self.db["users"]

    def get_user(self, cookie: dict):
        user = GetUser(cookie=cookie)
        current_user = user.get_me()
        return current_user

    def check_if_user_exists(self, user_id):
        return self.user_collection.count_documents({"user_id": user_id}, limit=1) != 0

    def add_user(self, user_id, user_name):
        user = {"user_id": user_id, "user_name": user_name}
        result = self.user_collection.insert_one(user)
        return result.inserted_id

    def get_user_by_id(self, user_id):
        user = self.user_collection.find_one({"user_id": user_id})
        return user
