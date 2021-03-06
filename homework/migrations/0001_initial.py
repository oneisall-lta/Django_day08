# Generated by Django 2.1 on 2018-08-14 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gname', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stuname', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('sex', models.IntegerField(choices=[(1, '男'), (2, '女')], default=1)),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homework.Grade')),
            ],
        ),
    ]
