# Generated by Django 4.1.5 on 2023-01-17 16:47

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Fanfic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, unique=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='media/', validators=[django.core.validators.FileExtensionValidator(['jpg'])])),
                ('description', models.CharField(blank=True, default='there is not any description', max_length=255)),
                ('date_created', models.CharField(blank=True, max_length=25, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FanficGenres',
            fields=[
                ('slug', models.SlugField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='FanficPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter', models.CharField(blank=True, default='Глава', max_length=20)),
                ('text', models.CharField(max_length=1000, null=True)),
                ('fanfic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='page', to='fanfic.fanfic')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='fanfic',
            name='genre',
            field=models.ForeignKey(blank=True, default='Other', on_delete=django.db.models.deletion.SET_DEFAULT, to='fanfic.fanficgenres'),
        ),
        migrations.AddField(
            model_name='fanfic',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]