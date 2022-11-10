# Generated by Django 4.1.2 on 2022-10-30 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlockedStock',
            fields=[
                ('stock_name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('update_time', models.DateTimeField()),
                ('type', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'blocked_stock',
            },
        ),
        migrations.CreateModel(
            name='FailedStock',
            fields=[
                ('stock_name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('update_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'failed_stock',
            },
        ),
        migrations.CreateModel(
            name='StockList',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('stock_name', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'db_table': 'stock_list',
            },
        ),
        migrations.CreateModel(
            name='StagnatingStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('stock_name', models.CharField(max_length=20)),
                ('type', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'stagnating_stock',
                'unique_together': {('type', 'date', 'stock_name')},
            },
        ),
        migrations.CreateModel(
            name='GoodStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('stock_name', models.CharField(max_length=20)),
                ('strength', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'good_stock',
                'unique_together': {('date', 'stock_name')},
            },
        ),
        migrations.CreateModel(
            name='IndexVolume',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('date', models.CharField(max_length=12)),
                ('index', models.FloatField()),
                ('index_open', models.FloatField()),
                ('index_low', models.FloatField()),
                ('index_high', models.FloatField()),
                ('volume', models.PositiveBigIntegerField()),
                ('ma_5', models.FloatField()),
                ('ma_10', models.FloatField()),
                ('ma_20', models.FloatField()),
                ('ma_50', models.FloatField()),
                ('ma_60', models.FloatField()),
                ('ma_150', models.FloatField()),
                ('ma_200', models.FloatField()),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock_indices.stocklist')),
            ],
            options={
                'db_table': 'index_volume',
                'unique_together': {('date', 'stock_id')},
            },
        ),
    ]