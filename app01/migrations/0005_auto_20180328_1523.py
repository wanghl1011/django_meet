# Generated by Django 2.0.2 on 2018-03-28 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_auto_20180328_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderrecord',
            name='meet_room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='record', to='app01.MeetingRoom', verbose_name='会议室'),
        ),
        migrations.AlterField(
            model_name='orderrecord',
            name='time_slot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='record', to='app01.TimeSlot'),
        ),
    ]
