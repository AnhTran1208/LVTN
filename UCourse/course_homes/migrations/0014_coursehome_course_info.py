# Generated by Django 3.0.3 on 2020-04-20 14:04

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_homes', '0013_coursehome_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursehome',
            name='course_info',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]