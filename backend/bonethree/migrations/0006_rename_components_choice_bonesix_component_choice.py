# Generated by Django 4.2.5 on 2023-09-22 05:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bonethree', '0005_bonefive_boneseven_bonesix'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bonesix',
            old_name='components_choice',
            new_name='component_choice',
        ),
    ]
