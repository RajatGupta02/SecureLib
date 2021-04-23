# Generated by Django 3.2 on 2021-04-22 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarymanager', '0004_book_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='IssueRequest',
            fields=[
                ('request_id', models.AutoField(primary_key=True, serialize=False)),
                ('book_name', models.CharField(max_length=50)),
                ('student_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('duration', models.IntegerField(default=7)),
                ('phone', models.IntegerField(max_length=10)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]