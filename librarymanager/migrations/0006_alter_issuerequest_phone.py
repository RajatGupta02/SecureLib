# Generated by Django 3.2 on 2021-04-22 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarymanager', '0005_issuerequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuerequest',
            name='phone',
            field=models.CharField(max_length=12),
        ),
    ]
