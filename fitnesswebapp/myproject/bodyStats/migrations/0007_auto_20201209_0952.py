# Generated by Django 3.1.2 on 2020-12-09 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bodyStats', '0006_auto_20201209_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='body_stats_tbl',
            name='height',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Height cm'),
        ),
        migrations.AlterField(
            model_name='body_stats_tbl',
            name='weight',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Weight kg'),
        ),
    ]
