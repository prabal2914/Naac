# Generated by Django 4.2.5 on 2023-10-10 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bonethree', '0018_alter_boneseven_choice'),
    ]

    operations = [
        migrations.AddField(
            model_name='btwoone',
            name='year',
            field=models.CharField(default=2012, max_length=5),
            preserve_default=False,
        ),
    ]