# Generated by Django 3.1.4 on 2020-12-07 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_custom_user_t_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='custom_user',
            old_name='t_name',
            new_name='tasks',
        ),
    ]
