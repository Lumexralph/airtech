# Generated by Django 2.2.3 on 2019-07-23 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0003_auto_20190719_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='flight_type',
            field=models.CharField(max_length=50),
        ),
    ]
