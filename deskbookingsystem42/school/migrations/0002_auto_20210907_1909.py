# Generated by Django 3.1.13 on 2021-09-07 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
