# Generated by Django 4.1.7 on 2023-04-21 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intro', '0003_aboutcontent_download_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree_title', models.CharField(max_length=100)),
                ('school_name', models.CharField(max_length=100)),
                ('graduation_date', models.CharField(max_length=100)),
                ('award', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('level', models.IntegerField()),
            ],
        ),
    ]
