# Generated by Django 3.0.3 on 2020-04-10 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_auto_20200410_0915'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionkit',
            name='modified_date',
            field=models.DateField(auto_now=True),
        ),
    ]
