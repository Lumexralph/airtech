# Generated by Django 2.2.3 on 2019-07-19 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]