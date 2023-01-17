# Generated by Django 4.1.5 on 2023-01-17 16:47

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='AnimeSeason',
            fields=[
                ('slug', models.SlugField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30, unique=True)),
                ('own_anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seasons', to='anime.anime')),
            ],
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('slug', models.SlugField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30, unique=True)),
                ('video', models.FileField(blank=True, null=True, upload_to='media/', validators=[django.core.validators.FileExtensionValidator(['mp4'])])),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='episodes', to='anime.animeseason')),
            ],
        ),
    ]