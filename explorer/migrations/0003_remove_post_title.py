# Generated by Django 3.0.4 on 2020-06-22 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('explorer', '0002_post_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
    ]
