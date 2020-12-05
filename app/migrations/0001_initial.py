# Generated by Django 3.1.4 on 2020-12-05 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mult',
            fields=[
                ('lid', models.IntegerField(primary_key=True, serialize=False)),
                ('count', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='speaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lid', models.IntegerField(default=0)),
                ('speak', models.FileField(default='default.mp3', upload_to='')),
                ('num', models.IntegerField(default=0)),
            ],
        ),
    ]
