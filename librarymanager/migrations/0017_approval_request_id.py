# Generated by Django 3.2 on 2021-04-25 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarymanager', '0016_rename_request_id_approval_request_id_old'),
    ]

    operations = [
        migrations.AddField(
            model_name='approval',
            name='request_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
