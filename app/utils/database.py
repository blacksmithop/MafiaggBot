from pymongo import MongoClient
from urllib.parse import quote_plus
from mafiagg.user import GetUser

username = quote_plus('user')
password = quote_plus('password')
uri = 'mongodb://%s:%s@localhost' % (username, password)

class UserCollection:
    def __init__(self):
        self.client = MongoClient(uri)
        self.db = self.client['mafiagg']
        self.user_collection = self.db['users']


    def get_user(self, cookie: dict):
        user = GetUser(cookie=cookie)
        current_user = user.get_me()
        return current_user
    
    def check_if_user_exists(self, user_id):
        return self.user_collection.count_documents({ 'user_id': user_id }, limit = 1) != 0

    def add_user(self, user_id, user_name):
        user = {
            "user_id": user_id,
            "user_name": user_name
        }
        result = self.user_collection.insert_one(user)
        return result.inserted_id

    def get_user_by_id(self, user_id):
        user = self.user_collection.find_one({"user_id": user_id})
        return user

    
# def add_user_game_report(self, user_id, game_report):
#     report = {
#         "user_id": user_id,
#         "game_report": game_report
#     }
#     result = self.reports_collection.insert_one(report)
#     return result.inserted_id

# def get_user_game_report(self, user_id):
#     reports = list(self.reports_collection.find({"user_id": user_id}))
#     return reports

# def get_notifications_by_user_id(self, user_id):
#     notifications = list(self.notifications_collection.find({"user_id": user_id}))
#     return notifications