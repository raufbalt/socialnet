# Generated by Django 4.1.5 on 2023-01-15 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fanfic', '0003_fanfic_date_created'),
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fanficcomment',
            name='fanfic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='fanfic.fanfic'),
        ),
    ]