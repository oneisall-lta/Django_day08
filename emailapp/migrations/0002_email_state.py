# Generated by Django 2.1 on 2018-08-15 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emailapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='state',
            field=models.IntegerField(default=0),
        ),
    ]