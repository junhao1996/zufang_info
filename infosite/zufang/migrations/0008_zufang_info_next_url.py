# Generated by Django 2.0.7 on 2018-07-26 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zufang', '0007_auto_20180726_0259'),
    ]

    operations = [
        migrations.AddField(
            model_name='zufang_info',
            name='next_url',
            field=models.CharField(default='', max_length=200),
        ),
    ]
