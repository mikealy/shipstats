# Generated by Django 2.2.6 on 2020-03-31 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0003_auto_20200330_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='boxplotstat',
            name='ship_primary_median',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=6),
        ),
        migrations.AddField(
            model_name='boxplotstat',
            name='ship_primary_neg2sigma',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=6),
        ),
        migrations.AddField(
            model_name='boxplotstat',
            name='ship_primary_pos2sigma',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=6),
        ),
        migrations.AddField(
            model_name='boxplotstat',
            name='ship_primary_q1',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=6),
        ),
        migrations.AddField(
            model_name='boxplotstat',
            name='ship_primary_q2',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=6),
        ),
    ]