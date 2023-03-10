# Generated by Django 4.1.5 on 2023-01-30 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_model', models.CharField(max_length=100)),
                ('loan_amount', models.FloatField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateField()),
                ('interest_rate', models.FloatField()),
            ],
            options={
                'db_table': 'carro',
            },
        ),
    ]
