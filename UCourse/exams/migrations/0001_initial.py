# Generated by Django 3.0.3 on 2020-05-06 16:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0015_course_fee_type'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0007_auto_20200419_0012'),
        ('course_homes', '0015_learningtopic_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbilityTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=10, unique=True)),
                ('duration', models.IntegerField()),
                ('status', models.BooleanField(default=True)),
                ('num_questions', models.IntegerField(blank=True, default=10, null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('course', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ability_test', to='courses.Course')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ability_creator', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(db_index=True, max_length=10, unique=True)),
                ('exam_type', models.CharField(choices=[('lt', 'Regular Lesson Quiz'), ('mc', 'Middle Course Test'), ('fc', 'Final Course Test')], max_length=2)),
                ('duration', models.IntegerField(blank=True, null=True)),
                ('pass_score', models.FloatField(max_length=3)),
                ('status', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='exam_creator', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='exam_modifier', to=settings.AUTH_USER_MODEL)),
                ('questions', models.ManyToManyField(related_name='question_exams', to='questions.Question')),
            ],
        ),
        migrations.CreateModel(
            name='UserAbilityTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_taken', models.DateTimeField(default=django.utils.timezone.now)),
                ('result', models.IntegerField(blank=True, null=True)),
                ('ability_test', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ability_user_test', to='exams.AbilityTest')),
                ('questions', models.ManyToManyField(related_name='ability_questions', to='questions.Question')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_ability_test', to=settings.AUTH_USER_MODEL)),
                ('user_responses', models.ManyToManyField(related_name='responses_users', to='questions.Choice')),
            ],
        ),
        migrations.CreateModel(
            name='UserResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_res', to='questions.Choice')),
                ('user_ability_test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_r', to='exams.UserAbilityTest')),
            ],
        ),
        migrations.CreateModel(
            name='StudentExam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_taken', models.DateTimeField(default=django.utils.timezone.now)),
                ('result', models.FloatField(blank=True, null=True)),
                ('exam', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_exams', to='exams.Exam')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='exam_students', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choices', models.ManyToManyField(to='questions.Choice')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Question')),
                ('student_exam', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='responses', to='exams.StudentExam')),
            ],
        ),
        migrations.AddField(
            model_name='exam',
            name='students',
            field=models.ManyToManyField(related_name='student_exams', through='exams.StudentExam', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='exam',
            name='topic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='topic_exams', to='course_homes.LearningTopic'),
        ),
        migrations.AddField(
            model_name='abilitytest',
            name='taken_users',
            field=models.ManyToManyField(related_name='ability_tests', through='exams.UserAbilityTest', to=settings.AUTH_USER_MODEL),
        ),
    ]
