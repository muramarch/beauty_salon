# Generated by Django 4.1.7 on 2023-08-01 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0003_remove_appointment_duration_minutes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]