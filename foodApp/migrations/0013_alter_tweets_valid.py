# Generated by Django 4.0.4 on 2022-08-29 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodApp', '0012_alter_tweets_valid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweets',
            name='valid',
            field=models.BooleanField(null=True),
        ),
    ]
