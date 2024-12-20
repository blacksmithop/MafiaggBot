from pymongo import MongoClient, ASCENDING, DESCENDING
from app.utils.database import uri
from app.utils.models import ChatMessage


class ChatCollection:
    def __init__(self):
        self.client = MongoClient(uri)
        self.db = self.client["mafiagg"]
        self.chat_collection = self.db["chat"]

    def add_message_to_db(self, chat_payload: ChatMessage):
        return self.chat_collection.insert_one(chat_payload)

    def get_chat_between_users(self, user_a, user_b):
        # Fetch all messages between user_a and user_b, sorted by timestamp
        query = {
            "$or": [
                {"senderId": user_a, "receiverId": user_b},
                {"senderId": user_b, "receiverId": user_a},
            ]
        }
        messages = self.chat_collection.find(query).sort("timestamp", ASCENDING)
        return list(messages)  # Convert to a list for easier use

    def get_latest_messages_to_user(self, user_id):
        # Aggregation to get the latest message sent to a specific user from each sender
        pipeline = [
            {"$match": {"receiverId": user_id}},  # Messages sent to user_id
            {"$sort": {"timestamp": DESCENDING}},  # Sort by timestamp descending
            {
                "$group": {
                    "_id": "$senderId",  # Group by senderId
                    "latestMessage": {"$first": "$$ROOT"},  # Get the latest message
                }
            },
            {"$replaceRoot": {"newRoot": "$latestMessage"}},  # Flatten the output
        ]
        messages = self.chat_collection.aggregate(pipeline)
        return list(messages)  # Convert to a list for easier use
