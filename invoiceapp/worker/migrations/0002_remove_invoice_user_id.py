# Generated by Django 3.1.4 on 2020-12-06 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='user_id',
        ),
    ]