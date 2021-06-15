# Generated by Django 3.2 on 2021-06-15 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websell', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demo',
            name='date',
        ),
        migrations.AddField(
            model_name='demo',
            name='day',
            field=models.DateTimeField(auto_now=True, db_column='day', verbose_name='Día'),
        ),
        migrations.AddField(
            model_name='demo',
            name='hour',
            field=models.TimeField(auto_now=True, db_column='hour', verbose_name='Hora'),
        ),
        migrations.AlterField(
            model_name='demo',
            name='surnames',
            field=models.CharField(db_column='surnames', max_length=100, verbose_name='Apellidos'),
        ),
    ]