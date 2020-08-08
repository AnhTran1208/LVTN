# Generated by Django 3.0.3 on 2020-04-03 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0008_auto_20200403_1250'),
        ('courses', '0007_auto_20200401_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='field',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='field_courses', to='programs.Field'),
        ),
        migrations.AlterField(
            model_name='course',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='courses/icon'),
        ),
    ]
