# Generated by Django 4.1.7 on 2023-04-22 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intro', '0008_rename_project_description_project_project_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='custom_description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]