# Generated by Django 4.2.4 on 2023-08-25 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv_projects', '0002_alter_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.CharField(max_length=100),
        ),
    ]
