# Generated by Django 4.2.5 on 2023-09-24 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bonethree', '0013_bfiveeight_bfiveeleven_bfivefive_bfivefour_bfivenine_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bseveneight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('add_info', models.CharField(max_length=150)),
                ('link', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Bseveneleven',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Bsevenfive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=1000)),
                ('photo', models.CharField(max_length=100)),
                ('report', models.CharField(max_length=250)),
                ('policy_doc', models.CharField(max_length=250)),
                ('link', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Bsevenfour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facilities', models.CharField(max_length=500)),
                ('option', models.CharField(max_length=150)),
                ('link', models.CharField(max_length=100)),
                ('photo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Bsevennine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('details', models.CharField(max_length=250)),
                ('link', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Bsevenone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('add_info', models.CharField(max_length=150)),
                ('link', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Bsevenseven',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('add_info', models.CharField(max_length=150)),
                ('link', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Bsevensix',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initiative', models.CharField(max_length=500)),
                ('option', models.CharField(max_length=150)),
                ('link', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Bseventen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_conduct', models.CharField(max_length=200)),
                ('option', models.CharField(max_length=150)),
                ('link', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Bseventhree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('add_info', models.CharField(max_length=150)),
                ('link', models.CharField(max_length=100)),
                ('photo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Bseventwelve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('webpage_link', models.CharField(max_length=150)),
                ('add_info', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Bseventwo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alt_source', models.CharField(max_length=500)),
                ('option', models.CharField(max_length=150)),
                ('link', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Bsixeight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=150)),
                ('purpose', models.CharField(max_length=100)),
                ('funds_receive', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Bsixeleven',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('add_info', models.CharField(max_length=150)),
                ('link', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Bsixfive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=500)),
                ('title', models.CharField(max_length=150)),
                ('name_teacher', models.CharField(max_length=100)),
                ('amount_HEI', models.CharField(max_length=100)),
                ('purpose', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Bsixfour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('add_info', models.CharField(max_length=150)),
                ('link', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Bsixnine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('add_info', models.CharField(max_length=150)),
                ('link', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Bsixone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('add_info', models.CharField(max_length=150)),
                ('link', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Bsixseven',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('add_info', models.CharField(max_length=150)),
                ('link', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Bsixsix',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_faculty', models.CharField(max_length=500)),
                ('type_prog', models.CharField(max_length=150)),
                ('duration', models.CharField(max_length=100)),
                ('start_end_date', models.CharField(max_length=100)),
                ('name_inst', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Bsixten',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('add_info', models.CharField(max_length=150)),
                ('link', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Bsixthree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=500)),
                ('option', models.CharField(max_length=150)),
                ('exp_stat', models.CharField(max_length=150)),
                ('egov_report', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Bsixtwelve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qual_insurance', models.CharField(max_length=500)),
                ('option', models.CharField(max_length=150)),
                ('link', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Bsixtwo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('inst_docs', models.CharField(max_length=150)),
                ('add_info', models.CharField(max_length=150)),
                ('link', models.CharField(max_length=100)),
            ],
        ),
    ]
