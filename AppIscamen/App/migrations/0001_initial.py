# Generated by Django 4.1.1 on 2023-10-26 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Liberacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_horarios', models.DateTimeField()),
                ('sector', models.CharField(max_length=50)),
                ('temp_humedad_entrega_cajas', models.FloatField()),
                ('temp_humedad_ingreso_sector_liberacion', models.FloatField()),
                ('millones_liberados', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Produccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('lotes', models.IntegerField()),
                ('millones_procesados', models.IntegerField()),
                ('cantidad_torres', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RECP_PUPA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('horarios', models.TimeField()),
                ('temperatura', models.FloatField()),
                ('litros', models.IntegerField()),
                ('lotes', models.IntegerField()),
            ],
        ),
    ]
