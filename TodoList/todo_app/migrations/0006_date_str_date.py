# Generated by Django 4.0.6 on 2023-05-08 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0005_todo_str_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='date',
            name='str_date',
            field=models.CharField(default='2023-05-08', max_length=30),
        ),
    ]
