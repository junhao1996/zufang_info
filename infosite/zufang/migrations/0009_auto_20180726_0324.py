# Generated by Django 2.0.7 on 2018-07-26 03:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zufang', '0008_zufang_info_next_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zufang_info',
            name='jjr',
        ),
        migrations.RemoveField(
            model_name='zufang_info',
            name='jjr_img',
        ),
        migrations.RemoveField(
            model_name='zufang_info',
            name='jjr_phone',
        ),
    ]