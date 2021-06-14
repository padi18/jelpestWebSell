# Generated by Django 3.2.4 on 2021-06-14 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Demo',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False, verbose_name='ID Demo')),
                ('name', models.CharField(db_column='name', max_length=50, verbose_name='Nombre')),
                ('surnames', models.CharField(db_column='surnames', max_length=50, verbose_name='Apellidos')),
                ('email', models.EmailField(db_column='email', max_length=254, verbose_name='Correo electrónico')),
                ('phone', models.CharField(db_column='phone', max_length=50, verbose_name='Teléfono')),
                ('date', models.DateTimeField(db_column='date', verbose_name='Dia y Hora')),
                ('restaurant_name', models.CharField(db_column='restaurant_name', max_length=100, verbose_name='Nombre del restaurante')),
            ],
            options={
                'db_table': 'demos',
            },
        ),
    ]
