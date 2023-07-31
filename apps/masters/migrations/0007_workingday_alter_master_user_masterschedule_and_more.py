# Generated by Django 4.1.7 on 2023-07-31 05:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('masters', '0006_remove_master_schedule_alter_master_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkingDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_week', models.PositiveIntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')])),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='master',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_master', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='MasterSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='master_schedule', to='masters.master')),
                ('working_days', models.ManyToManyField(to='masters.workingday')),
            ],
        ),
        migrations.AddField(
            model_name='master',
            name='schedule',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='master_schedule', to='masters.masterschedule'),
        ),
    ]