# Generated by Django 4.0.4 on 2022-08-29 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodApp', '0010_tweetfile_tweets'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweets',
            name='valid',
            field=models.BooleanField(null=True),
        ),
    ]