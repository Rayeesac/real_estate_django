# Generated by Django 3.2 on 2024-01-06 03:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='features',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
