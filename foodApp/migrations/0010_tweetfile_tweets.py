# Generated by Django 4.0.4 on 2022-08-29 07:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodApp', '0009_publication'),
    ]

    operations = [
        migrations.CreateModel(
            name='TweetFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media', models.FileField(upload_to='images')),
                ('tweep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tweets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texts', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('file_content', models.ManyToManyField(blank=True, related_name='file_content', to='foodApp.tweetfile')),
                ('tweep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Tweets',
            },
        ),
    ]
