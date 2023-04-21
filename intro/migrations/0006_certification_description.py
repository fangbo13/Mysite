# Generated by Django 4.1.7 on 2023-04-21 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intro', '0005_rename_name_skill_skill_icon_remove_skill_level_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certification', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_title', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]