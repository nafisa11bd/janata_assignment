# Generated by Django 4.1.4 on 2022-12-26 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0005_alter_stockinfo_tradecode'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stockinfo',
            old_name='tradecode',
            new_name='trade_code',
        ),
    ]
