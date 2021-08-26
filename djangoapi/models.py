from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import SET_NULL
from django.conf import settings
from django.db.models.signals import post_save

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
    reciever = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reciever")
    content = models.CharField(max_length=300, default="")
    subject = models.CharField(max_length=40)
    date_create = models.DateTimeField(auto_now_add=True, null=True)
    readed = models.BooleanField(default=False)

def __str__(self):
        return self.subject
