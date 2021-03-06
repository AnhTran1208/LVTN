# Generated by Django 3.0.3 on 2020-06-07 14:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0018_remove_course_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserBuyCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bought_date', models.DateField(default=django.utils.timezone.now)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='user_buy',
            field=models.ManyToManyField(related_name='buy_courses', through='courses.UserBuyCourse', to=settings.AUTH_USER_MODEL),
        ),
    ]
