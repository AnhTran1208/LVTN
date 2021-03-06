# Generated by Django 3.0.3 on 2020-05-31 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_homes', '0016_auto_20200530_2313'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursehome',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='coursehome',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
