# Generated by Django 4.0.4 on 2022-08-06 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodApp', '0002_utilisateur_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(max_length=300)),
                ('Description', models.TextField(max_length=300)),
            ],
            options={
                'verbose_name': 'Ingredient',
                'verbose_name_plural': 'Ingredients',
            },
        ),
        migrations.CreateModel(
            name='Plat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=300)),
                ('description', models.TextField(max_length=300)),
                ('photo', models.ImageField(upload_to='')),
                ('plat_national', models.BooleanField()),
                ('recette', models.TextField(max_length=5000)),
                ('ingredients', models.ManyToManyField(to='foodApp.ingredient')),
                ('pays', models.ManyToManyField(to='foodApp.pays')),
            ],
            options={
                'verbose_name': 'Plat',
                'verbose_name_plural': 'Plats',
            },
        ),
    ]
