# Generated by Django 3.0.3 on 2020-04-18 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_homes', '0009_auto_20200418_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursehome',
            name='code',
        ),
    ]
