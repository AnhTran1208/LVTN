# Generated by Django 3.0.3 on 2020-03-28 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20200328_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
