# Generated by Django 4.1.7 on 2023-04-21 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=200)),
                ('background_image', models.ImageField(upload_to='background/')),
                ('photo', models.ImageField(upload_to='myphoto/')),
                ('Eng_content', models.CharField(max_length=200)),
                ('Ire_content', models.CharField(max_length=200)),
            ],
        ),
    ]