from pymongo import MongoClient, DESCENDING
from app.utils.database import uri
from app.utils.models import BaseNotification, GameInvitePayload, PlayerGameReportPayload, FriendRequestPayload
from datetime import datetime


class NotificationCollection:
    def __init__(self):
        self.client = MongoClient(uri)
        self.db = self.client["mafiagg"]
        self.notification_collection = self.db["notifications"]
        self._setup_indexes()

    def _setup_indexes(self):
        # Ensure indexes for efficient querying
        self.notification_collection.create_index("user_id")
        self.notification_collection.create_index("type")
        self.notification_collection.create_index("timestamp")
        self.notification_collection.create_index("read")

    def add_notification(self, user_id: int, notification_type: str, content: dict):
        # Create and add a notification
        notification = BaseNotification(user_id=user_id, type=notification_type, content=content)
        result = self.notification_collection.insert_one(notification.dict())
        return result.inserted_id

    def get_notifications(self, user_id: int, unread_only: bool = False, page: int = 1, page_size: int = 20):
        # Fetch notifications for a user, optionally filtering unread notifications
        query = {"user_id": user_id}
        if unread_only:
            query["read"] = False
        notifications = (
            self.notification_collection.find(query)
            .sort("timestamp", DESCENDING)
            .skip((page - 1) * page_size)
            .limit(page_size)
        )
        return [BaseNotification(**notif) for notif in notifications]

    def mark_notification_as_read(self, notification_id: str):
        # Mark a notification as read
        result = self.notification_collection.update_one(
            {"_id": notification_id}, {"$set": {"read": True}}
        )
        return result.modified_count > 0

    def delete_notification(self, notification_id: str):
        # Delete a notification
        result = self.notification_collection.delete_one({"_id": notification_id})
        return result.deleted_count > 0

    def get_unread_count(self, user_id: int):
        # Get the count of unread notifications for a user
        return self.notification_collection.count_documents({"user_id": user_id, "read": False})
