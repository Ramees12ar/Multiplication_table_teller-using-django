# Generated by Django 3.1.4 on 2020-12-05 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0006_auto_20201205_0915'),
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
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('lid', models.IntegerField(default='1')),
                ('speak', models.FileField(default='default.mp3', upload_to='')),
                ('num', models.IntegerField(default='1')),
            ],
        ),
    ]