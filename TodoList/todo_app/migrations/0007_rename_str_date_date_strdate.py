# Generated by Django 4.0.6 on 2023-05-08 02:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0006_date_str_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='date',
            old_name='str_date',
            new_name='strdate',
        ),
    ]
