# Generated by Django 3.0.3 on 2020-04-09 12:55

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0014_auto_20200406_1640'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('code', models.CharField(max_length=10, unique=True)),
                ('content', ckeditor.fields.RichTextField()),
                ('question_type', models.CharField(choices=[('mc', 'Multi choices'), ('tf', 'True false'), ('tx', 'Paragraph text question')], default='mc', max_length=2)),
                ('difficult_level', models.CharField(choices=[('e', 'Easy'), ('m', 'Medium'), ('h', 'Hard')], max_length=1)),
                ('score', models.FloatField(blank=True, default=1.0, null=True)),
                ('status', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionKit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=10, unique=True)),
                ('status', models.BooleanField(default=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('created_by', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='kit_creator', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='kit_modifier', to=settings.AUTH_USER_MODEL)),
                ('skill', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='skill_question_kits', to='courses.Skill')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('content', models.TextField()),
                ('is_answer', models.BooleanField(blank=True, default=False, null=True)),
                ('status', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='questions.Question')),
            ],
        ),
    ]
