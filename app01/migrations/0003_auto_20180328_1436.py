# Generated by Django 2.0.2 on 2018-03-28 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20180327_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetingroom',
            name='row',
            field=models.CharField(default=1, max_length=10, verbose_name='该会议室在表格中是第几行'),
        ),
        migrations.AddField(
            model_name='timeslot',
            name='col',
            field=models.CharField(default=1, max_length=10, verbose_name='该时间段在表格中是第几列'),
        ),
    ]