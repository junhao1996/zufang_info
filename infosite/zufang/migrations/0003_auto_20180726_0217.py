# Generated by Django 2.0.7 on 2018-07-26 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zufang', '0002_zufang_info_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='zufang_info',
            name='jjr',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='zufang_info',
            name='jjr_img',
            field=models.CharField(default='', max_length=300),
        ),
    ]