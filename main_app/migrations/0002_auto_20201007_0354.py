# Generated by Django 3.1.2 on 2020-10-07 03:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='gives_rewards',
            new_name='rewards',
        ),
    ]
