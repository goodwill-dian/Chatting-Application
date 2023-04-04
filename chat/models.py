from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Messagge(models.Model):
    sender = models.ForeignKey(User, related_name='message', on_delete=models.CASCADE)
    context = models.TextField()
    send_time = models.DateTimeField(auto_now_add=True)