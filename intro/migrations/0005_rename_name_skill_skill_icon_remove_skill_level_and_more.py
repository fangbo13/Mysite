# Generated by Django 4.1.7 on 2023-04-21 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intro', '0004_education_skill'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skill',
            old_name='name',
            new_name='skill_icon',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='level',
        ),
        migrations.AddField(
            model_name='skill',
            name='skill_level',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skill',
            name='skill_name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
