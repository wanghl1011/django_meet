# Generated by Django 2.0.2 on 2018-03-28 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_auto_20180328_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetingroom',
            name='row',
            field=models.IntegerField(default=1, max_length=10, verbose_name='该会议室在表格中是第几行'),
        ),
        migrations.AlterField(
            model_name='orderrecord',
            name='col',
            field=models.IntegerField(blank=True, max_length=10, null=True, verbose_name='列'),
        ),
        migrations.AlterField(
            model_name='orderrecord',
            name='row',
            field=models.IntegerField(blank=True, max_length=10, null=True, verbose_name='行'),
        ),
        migrations.AlterField(
            model_name='timeslot',
            name='col',
            field=models.IntegerField(default=1, max_length=10, verbose_name='该时间段在表格中是第几列'),
        ),
    ]
