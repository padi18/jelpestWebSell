# Generated by Django 3.2 on 2021-06-15 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websell', '0003_alter_demo_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demo',
            name='day',
            field=models.DateField(db_column='day', verbose_name='Día'),
        ),
        migrations.AlterField(
            model_name='demo',
            name='hour',
            field=models.TimeField(db_column='hour', verbose_name='Hora'),
        ),
    ]
