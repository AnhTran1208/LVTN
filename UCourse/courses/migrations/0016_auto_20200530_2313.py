# Generated by Django 3.0.3 on 2020-05-30 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('courses', '0015_course_fee_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='course',
            name='open_date',
        ),
        migrations.AlterField(
            model_name='course',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], max_length=10),
        ),
        migrations.AlterField(
            model_name='course',
            name='teacher',
            field=models.ManyToManyField(blank=True, limit_choices_to={'is_teacher': True}, related_name='courses_tutors', to='profiles.Profile'),
        ),
    ]
