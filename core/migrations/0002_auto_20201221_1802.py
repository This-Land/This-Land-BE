# Generated by Django 3.1.4 on 2020-12-21 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pointofinterest',
            name='user',
        ),
        migrations.RemoveField(
            model_name='tellyourstory',
            name='user',
        ),
    ]