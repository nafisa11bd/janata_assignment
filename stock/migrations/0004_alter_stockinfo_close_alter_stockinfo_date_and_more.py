# Generated by Django 4.1.4 on 2022-12-25 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_alter_stockinfo_close_alter_stockinfo_high_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockinfo',
            name='close',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='stockinfo',
            name='date',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='stockinfo',
            name='high',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='stockinfo',
            name='low',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='stockinfo',
            name='open',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='stockinfo',
            name='volume',
            field=models.CharField(max_length=100),
        ),
    ]
