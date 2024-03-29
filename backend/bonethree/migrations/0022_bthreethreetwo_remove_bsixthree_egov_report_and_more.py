# Generated by Django 4.2.5 on 2023-10-31 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bonethree', '0021_btwofifteen_year_join_btwofourteen_year_btwoten_year_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bthreethreetwo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_awardee', models.CharField(max_length=500)),
                ('name_award', models.CharField(max_length=500)),
                ('name_body', models.CharField(max_length=500)),
                ('award_category', models.CharField(max_length=500)),
                ('award_year', models.CharField(max_length=500)),
            ],
        ),
        migrations.RemoveField(
            model_name='bsixthree',
            name='egov_report',
        ),
        migrations.RemoveField(
            model_name='bsixthree',
            name='exp_stat',
        ),
        migrations.AddField(
            model_name='bfiveeight',
            name='year',
            field=models.CharField(default=123, max_length=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bfivefive',
            name='year',
            field=models.CharField(default=123, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bfiveseven',
            name='level_exam',
            field=models.CharField(default=123, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bfivesix',
            name='year',
            field=models.CharField(default=123, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bfourtwo',
            name='year',
            field=models.CharField(default=123, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bsixsix',
            name='year',
            field=models.CharField(default=123, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bthreetwo',
            name='link',
            field=models.CharField(default=123, max_length=100),
            preserve_default=False,
        ),
    ]
