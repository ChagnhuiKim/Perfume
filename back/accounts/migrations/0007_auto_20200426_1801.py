# Generated by Django 3.0.4 on 2020-04-26 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200423_1527'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='survey',
            name='hate_notes',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='rnd',
        ),
    ]
