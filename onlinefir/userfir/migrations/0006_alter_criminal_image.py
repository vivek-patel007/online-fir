# Generated by Django 4.1.7 on 2023-03-22 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userfir', '0005_rename_criminl_criminal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='criminal',
            name='image',
            field=models.ImageField(upload_to='userfir/criminal'),
        ),
    ]
