# Generated by Django 2.2.3 on 2019-07-24 03:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_user_last_login'),
        ('flight', '0004_auto_20190723_0553'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='reservations',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='reserved_flights', to='account.User'),
        ),
    ]