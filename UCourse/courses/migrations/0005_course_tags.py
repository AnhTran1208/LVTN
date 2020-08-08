# Generated by Django 3.0.3 on 2020-03-29 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0005_auto_20200329_2051'),
        ('courses', '0004_course_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='course_tags', to='tags.Tag'),
        ),
    ]
