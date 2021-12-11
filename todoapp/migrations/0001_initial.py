# Generated by Django 3.1.4 on 2020-12-07 06:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=100)),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
                ('priority', models.CharField(max_length=100)),
                ('due_date', models.DateField()),
                ('is_completed', models.BooleanField(default=False, verbose_name='Completed')),
                ('notes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='custom_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]