# Generated by Django 4.2.5 on 2023-09-22 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bonethree', '0004_bonefour'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bonefive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('mode_course', models.CharField(max_length=150)),
                ('course_code', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=100)),
                ('hours', models.CharField(max_length=100)),
                ('st_enrolled', models.CharField(max_length=100)),
                ('st_completed', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Boneseven',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(max_length=1)),
                ('link', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Bonesix',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('code', models.CharField(max_length=100)),
                ('components_choice', models.CharField(max_length=100)),
                ('component_name', models.CharField(max_length=100)),
                ('component_code', models.CharField(max_length=100)),
                ('student', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=100)),
            ],
        ),
    ]
