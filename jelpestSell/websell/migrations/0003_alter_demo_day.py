# Generated by Django 3.2 on 2021-06-15 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websell', '0002_auto_20210615_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demo',
            name='day',
            field=models.DateField(auto_now=True, db_column='day', verbose_name='Día'),
        ),
    ]
