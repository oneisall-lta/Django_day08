from django.db import models


# Create your models here.
class Email(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    sender = models.CharField(max_length=10)

    state = models.IntegerField(default=0)  # 0表示未读，1是已读
