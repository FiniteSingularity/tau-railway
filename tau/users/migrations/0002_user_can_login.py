# Generated by Django 3.1.7 on 2021-05-20 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='can_login',
            field=models.BooleanField(default=True),
        ),
    ]
