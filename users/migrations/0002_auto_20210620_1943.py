# Generated by Django 3.2.4 on 2021-06-20 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
