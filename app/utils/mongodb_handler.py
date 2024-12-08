from pymongo import MongoClient
from urllib.parse import quote_plus


class UserRepository:
    def __init__(self, uri, db_name):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.users_collection = self.db['users']
        self.reports_collection = self.db['game_reports']
        self.notifications_collection = self.db['notifications']

    def add_user(self, user_id, user_name):
        user = {
            "user_id": user_id,
            "user_name": user_name
        }
        result = self.users_collection.insert_one(user)
        return result.inserted_id

    def get_user(self, user_id):
        user = self.users_collection.find_one({"user_id": user_id})
        return user

    def add_user_game_report(self, user_id, game_report):
        report = {
            "user_id": user_id,
            "game_report": game_report
        }
        result = self.reports_collection.insert_one(report)
        return result.inserted_id

    def get_user_game_report(self, user_id):
        reports = list(self.reports_collection.find({"user_id": user_id}))
        return reports

    def get_notifications_by_user_id(self, user_id):
        notifications = list(self.notifications_collection.find({"user_id": user_id}))
        return notifications

# Example usage
if __name__ == "__main__":
    username = quote_plus('user')
    password = quote_plus('password')

    # TODO: Use BaseModel schema
    uri = 'mongodb://%s:%s@localhost' % (username, password)
    print(uri)
    db_name = "game_db"
    
    user_repo = UserRepository(uri, db_name)
    
    # Add a user
    user_id = "user123"
    user_name = "John Doe"
    user_repo.add_user(user_id, user_name)

    # Get a user
    user = user_repo.get_user(user_id)
    print("User:", user)

    # Add a game report
    game_report = {
        "game": "chess",
        "score": 1500,
        "date": "2024-12-06"
    }
    user_repo.add_user_game_report(user_id, game_report)

    # Get user game reports
    reports = user_repo.get_user_game_report(user_id)
    print("User Game Reports:", reports)

    # Get notifications by user id
    notifications = user_repo.get_notifications_by_user_id(user_id)
    print("Notifications:", notifications)
