# Generated by Django 3.2 on 2021-04-23 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarymanager', '0010_alter_book_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Approval',
            fields=[
                ('request_id', models.AutoField(primary_key=True, serialize=False)),
                ('book_name', models.CharField(max_length=50)),
                ('student_name', models.CharField(max_length=50)),
                ('student_id', models.CharField(default='', max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('duration', models.PositiveIntegerField()),
                ('phone', models.CharField(max_length=12)),
                ('approvaldate', models.DateField(auto_now_add=True)),
            ],
        ),
    ]