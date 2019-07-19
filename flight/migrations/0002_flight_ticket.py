# Generated by Django 2.2.3 on 2019-07-19 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0002_auto_20190719_1500'),
        ('flight', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='ticket',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='flight', to='ticket.Ticket'),
        ),
    ]
