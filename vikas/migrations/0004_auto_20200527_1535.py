# Generated by Django 3.0.6 on 2020-05-27 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vikas', '0003_auto_20200527_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity_period',
            name='end_time1',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='activity_period',
            name='end_time2',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='activity_period',
            name='end_time3',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='activity_period',
            name='start_time1',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='activity_period',
            name='start_time2',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='activity_period',
            name='start_time3',
            field=models.CharField(max_length=50),
        ),
    ]
