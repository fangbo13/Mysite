# Generated by Django 4.1.7 on 2023-04-21 17:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('intro', '0002_rename_photo_homecontent_myphoto'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_title', models.CharField(max_length=200)),
                ('about_background', models.ImageField(upload_to='about_background/')),
                ('text_up', models.CharField(max_length=200)),
                ('text_down', models.CharField(max_length=200)),
                ('about_photo', models.ImageField(upload_to='about_photo/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Download',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('download', models.FileField(upload_to='download/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='homecontent',
            name='background_image',
        ),
        migrations.RemoveField(
            model_name='homecontent',
            name='myphoto',
        ),
        migrations.AddField(
            model_name='homecontent',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homecontent',
            name='home_background',
            field=models.ImageField(default=1, upload_to='home_background/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homecontent',
            name='home_photo',
            field=models.ImageField(default=1, upload_to='home_photo/'),
            preserve_default=False,
        ),
    ]
