# Generated by Django 4.2.4 on 2023-08-23 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv_projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FilePathField(path='/cv_projects/img'),
        ),
    ]
