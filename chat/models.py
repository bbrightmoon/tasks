from django.db import models
from user.models import User


class Room(models.Model):
    name = models.CharField(
        max_length=200
    )
    host = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="room"
    )
    current_users = models.ManyToManyField(
        User, related_name="current_rooms", blank=True)

    def __str__(self):
        return f"Room({self.name} {self.host})"


class Message(models.Model):
    text = models.TextField(
        max_length=500
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="messages"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE, related_name="messages"
    )

    def __str__(self):
        return f"Message({self.user} {self.room})"

