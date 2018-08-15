from django.db import models


# Create your models here.
class Cake(models.Model):
    name = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    price = models.FloatField()

    class Meta:
        verbose_name_plural = '蛋糕'
        db_table = 'cake'
