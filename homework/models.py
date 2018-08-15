from django.db import models


# Create your models here.
class Grade(models.Model):
    gname = models.CharField(max_length=10)


class Student(models.Model):
    stuname = models.CharField(max_length=10)
    age = models.IntegerField()
    sex = models.CharField(verbose_name='性别', max_length=10, choices=(('male', '男'), ('female', '女')), default='male')

    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
