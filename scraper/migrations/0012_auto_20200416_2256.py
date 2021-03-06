# Generated by Django 3.0.4 on 2020-04-17 02:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0011_auto_20200416_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ship',
            name='nation',
            field=models.ForeignKey(default=111, on_delete=django.db.models.deletion.CASCADE, to='scraper.Nation'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ship',
            name='type',
            field=models.ForeignKey(default=111, on_delete=django.db.models.deletion.CASCADE, to='scraper.ShipType'),
            preserve_default=False,
        ),
    ]
