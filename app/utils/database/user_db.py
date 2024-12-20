from pymongo import MongoClient, ASCENDING, DESCENDING
from mafiagg.user import GetUser
from app.utils.database import uri
from app.utils.models import PlayerStats
from datetime import datetime


class UserCollection:
    def __init__(self):
        self.client = MongoClient(uri)
        self.db = self.client["mafiagg"]
        self.user_collection = self.db["users"]
        self.friends_collection = self.db["friendships"]
        self._setup_indexes()

    def _setup_indexes(self):
        # Ensure indexes for efficient querying
        self.user_collection.create_index("user_id", unique=True)
        self.friends_collection.create_index([("user_id", ASCENDING), ("friend_id", ASCENDING)])
        self.friends_collection.create_index("status")
        self.friends_collection.create_index("updated_at")

    def get_user(self, cookie: dict):
        user = GetUser(cookie=cookie)
        current_user = user.get_me()
        return current_user

    def check_if_user_exists(self, user_id: int) -> bool:
        return self.user_collection.count_documents({"user_id": user_id}, limit=1) != 0

    def add_user(self, user_id: int, user_name: str):
        if self.check_if_user_exists(user_id):
            raise ValueError("User already exists")
        user_obj = PlayerStats(user_id=user_id, username=user_name)
        result = self.user_collection.insert_one(user_obj.dict())
        return result.inserted_id

    def get_user_by_id(self, user_id: int):
        return self.user_collection.find_one({"user_id": user_id})

    # Friend Request Functions
    def send_friend_request(self, user_id: int, friend_id: int):
        if not self.check_if_user_exists(user_id) or not self.check_if_user_exists(friend_id):
            raise ValueError("One or both users do not exist")
        existing = self.friends_collection.find_one({
            "$or": [
                {"user_id": user_id, "friend_id": friend_id},
                {"user_id": friend_id, "friend_id": user_id},
            ]
        })
        if existing:
            raise ValueError("Friendship or request already exists")
        friendship = {
            "user_id": user_id,
            "friend_id": friend_id,
            "status": "pending",
            "initiated_at": datetime.now(),
            "updated_at": datetime.now(),
        }
        result = self.friends_collection.insert_one(friendship)
        return result.inserted_id

    def accept_friend_request(self, user_id: int, friend_id: int):
        result = self.friends_collection.update_one(
            {"user_id": friend_id, "friend_id": user_id, "status": "pending"},
            {"$set": {"status": "accepted", "updated_at": datetime.now()}}
        )
        if result.modified_count == 0:
            raise ValueError("No pending friend request found")
        return True

    def remove_friend(self, user_id: int, friend_id: int):
        result = self.friends_collection.delete_one({
            "$or": [
                {"user_id": user_id, "friend_id": friend_id},
                {"user_id": friend_id, "friend_id": user_id},
            ]
        })
        return result.deleted_count > 0

    def block_user(self, user_id: int, friend_id: int):
        result = self.friends_collection.update_one(
            {"user_id": user_id, "friend_id": friend_id},
            {"$set": {"status": "blocked", "updated_at": datetime.now()}},
            upsert=True
        )
        return result.modified_count > 0

    def get_friends_list(self, user_id: int):
        friends = self.friends_collection.find({
            "$or": [
                {"user_id": user_id, "status": "accepted"},
                {"friend_id": user_id, "status": "accepted"},
            ]
        })
        return [
            {
                "friend_id": f["friend_id"] if f["user_id"] == user_id else f["user_id"],
                "status": f["status"],
                "updated_at": f["updated_at"],
            }
            for f in friends
        ]

    def get_pending_friend_requests(self, user_id: int):
        requests = self.friends_collection.find({
            "friend_id": user_id,
            "status": "pending"
        }).sort("initiated_at", ASCENDING)
        return list(requests)

    def get_unread_friend_requests_count(self, user_id: int):
        # Get the count of unread friend requests for a user
        return self.friends_collection.count_documents({
            "friend_id": user_id,
            "status": "pending"
        })
