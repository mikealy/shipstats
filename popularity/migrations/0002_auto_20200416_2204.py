# Generated by Django 3.0.4 on 2020-04-17 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('popularity', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shiprelation',
            old_name='ship1',
            new_name='ship_primary',
        ),
        migrations.RenameField(
            model_name='shiprelation',
            old_name='ship2',
            new_name='ship_secondary',
        ),
        migrations.AddField(
            model_name='shiprelation',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
