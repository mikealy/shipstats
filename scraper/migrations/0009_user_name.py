# Generated by Django 2.2.6 on 2020-01-29 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0008_auto_20200128_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='name', max_length=255),
            preserve_default=False,
        ),
    ]