# Generated by Django 4.2 on 2024-03-21 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='icourse',
            name='plus',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='icourse',
            name='premium',
            field=models.BooleanField(default=False),
        ),
    ]