# Generated by Django 3.1.2 on 2020-12-09 09:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bodyStats', '0005_auto_20201118_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='body_stats_tbl',
            name='bs_entry_id',
            field=models.AutoField(db_index=True, default=datetime.datetime.now, primary_key=True, serialize=False, unique=True, verbose_name='body stat entry id'),
        ),
    ]
