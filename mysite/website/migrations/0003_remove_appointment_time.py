# Generated by Django 4.1.4 on 2023-01-16 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_appointment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='time',
        ),
    ]