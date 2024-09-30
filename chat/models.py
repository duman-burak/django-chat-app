from django.db import models
from django.contrib.auth.models import User
import uuid 

class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    first_user = models.ForeignKey(User,related_name="first_user", verbose_name=("first-user"), on_delete=models.CASCADE)
    second_user = models.ForeignKey(User,related_name="second_user" ,verbose_name=("second-user"), on_delete=models.CASCADE)

class Message(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    room = models.ForeignKey(Room, verbose_name=("Oda"), on_delete=models.CASCADE)
    content = models.TextField(("Mesaj İçeriği"))
    date = models.DateTimeField(auto_now_add=True)
    type_control = models.CharField(max_length=50, null=True)
    def get_short_date(self):
        return str(self.date.hour) + ":" + str(self.date.minute)

class ChatRoom(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User, related_name='chat_rooms')

    def __str__(self):
        return self.name

class Mute(models.Model):
    muter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='muter')
    muted_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='muted_user')
    muted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.muter} muted {self.muted_user}"

class Block(models.Model):
    blocker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blocker')
    blocked_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blocked_user')
    blocked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.blocker} blocked {self.blocked_user}"