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
