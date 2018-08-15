# Generated by Django 2.1 on 2018-08-15 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cake',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=20)),
                ('price', models.FloatField()),
            ],
            options={
                'verbose_name_plural': '蛋糕',
                'db_table': 'cake',
            },
        ),
    ]
