# Generated by Django 3.2 on 2021-04-22 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarymanager', '0007_alter_issuerequest_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuerequest',
            name='duration',
            field=models.PositiveIntegerField(),
        ),
    ]
