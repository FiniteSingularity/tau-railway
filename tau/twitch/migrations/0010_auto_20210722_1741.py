# Generated by Django 3.1.7 on 2021-07-22 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitch', '0009_twitcheventsubsubscription_lookup_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='twitcheventsubsubscription',
            options={'ordering': ('name',)},
        ),
    ]
