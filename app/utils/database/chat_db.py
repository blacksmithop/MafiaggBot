from pymongo import MongoClient, ASCENDING, DESCENDING
from app.utils.database import uri
from app.utils.models import ChatMessage
from pydantic import ValidationError


class ChatCollection:
    def __init__(self):
        self.client = MongoClient(uri)
        self.db = self.client["mafiagg"]
        self.chat_collection = self.db["chat"]
        self._setup_indexes()

    def _setup_indexes(self):
        self.chat_collection.create_index([("senderId", ASCENDING), ("receiverId", ASCENDING)])
        self.chat_collection.create_index("timestamp")

    def add_message_to_db(self, chat_payload: ChatMessage):
        try:
            validated_payload = ChatMessage(**chat_payload.dict())
            result = self.chat_collection.insert_one(validated_payload.dict())
            return result.inserted_id
        except ValidationError as e:
            raise RuntimeError(f"Failed to insert message into database: {e}")

    def get_chat_between_users(self, user_a, user_b, page=1, page_size=50):
        query = {
            "$or": [
                {"senderId": user_a, "receiverId": user_b},
                {"senderId": user_b, "receiverId": user_a},
            ]
        }
        messages = (
            self.chat_collection.find(query)
            .sort("timestamp", ASCENDING)
            .skip((page - 1) * page_size)
            .limit(page_size)
        )
        return [ChatMessage(**msg) for msg in messages]

    def get_latest_messages_to_user(self, user_id):
        pipeline = [
            {"$match": {"receiverId": user_id}},
            {"$sort": {"timestamp": DESCENDING}},
            {
                "$group": {
                    "_id": "$senderId",
                    "latestMessage": {"$first": "$$ROOT"},
                }
            },
            {"$replaceRoot": {"newRoot": "$latestMessage"}},
        ]
        messages = self.chat_collection.aggregate(pipeline)
        return [ChatMessage(**msg) for msg in messages]
