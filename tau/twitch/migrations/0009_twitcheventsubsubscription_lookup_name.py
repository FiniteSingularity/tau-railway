# Generated by Django 3.1.7 on 2021-07-16 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitch', '0008_auto_20210715_2118'),
    ]

    operations = [
        migrations.AddField(
            model_name='twitcheventsubsubscription',
            name='lookup_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
