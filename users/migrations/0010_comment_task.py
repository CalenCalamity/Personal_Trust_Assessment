# Generated by Django 3.2.4 on 2021-06-20 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20210620_2003'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('task_title', models.CharField(max_length=80)),
                ('priority', models.CharField(max_length=2)),
                ('due_date', models.DateTimeField()),
                ('description', models.CharField(max_length=254)),
                ('assigned_user_email', models.CharField(max_length=254)),
                ('is_deleted', models.BooleanField()),
                ('last_modified_by_email', models.CharField(max_length=254)),
                ('created_date', models.DateTimeField()),
                ('last_modified_date', models.DateTimeField()),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.authuser')),
            ],
            options={
                'db_table': 'task',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('assigned_user_email', models.CharField(max_length=254)),
                ('message', models.CharField(max_length=254)),
                ('is_complete', models.BooleanField()),
                ('is_deleted', models.BooleanField()),
                ('last_modified_by_email', models.CharField(max_length=254)),
                ('created_date', models.DateTimeField()),
                ('last_modified_date', models.DateTimeField()),
                ('created_by_email', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.authuser')),
                ('task', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.task')),
            ],
            options={
                'db_table': 'task_comment',
                'managed': True,
            },
        ),
    ]
