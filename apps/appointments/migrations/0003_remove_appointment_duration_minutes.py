# Generated by Django 4.1.7 on 2023-07-30 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_appointment_duration_minutes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='duration_minutes',
        ),
    ]
