# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BlockedStock(models.Model):
    stock_name = models.CharField(primary_key=True, max_length=20)
    update_time = models.DateTimeField()
    type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'blocked_stock'


class FailedStock(models.Model):
    stock_name = models.CharField(primary_key=True, max_length=20)
    update_time = models.DateTimeField()

    class Meta:
        db_table = 'failed_stock'


class GoodStock(models.Model):
    date = models.DateField()
    stock_name = models.CharField(max_length=20)
    strength = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'good_stock'
        unique_together = (('date', 'stock_name'),)


class IndexVolume(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.CharField(max_length=12)
    stock = models.ForeignKey('StockList', to_field='id', on_delete=models.CASCADE)
    index = models.FloatField()
    index_open = models.FloatField()
    index_low = models.FloatField()
    index_high = models.FloatField()
    volume = models.PositiveBigIntegerField()
    ma_5 = models.FloatField()
    ma_10 = models.FloatField()
    ma_20 = models.FloatField()
    ma_50 = models.FloatField()
    ma_60 = models.FloatField()
    ma_150 = models.FloatField()
    ma_200 = models.FloatField()

    class Meta:
        db_table = 'index_volume'
        unique_together = (('date', 'stock_id'),)


class StagnatingStock(models.Model):
    date = models.DateField()
    stock_name = models.CharField(max_length=20)
    type = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'stagnating_stock'
        unique_together = (('type', 'date', 'stock_name'),)


class StockList(models.Model):
    id = models.AutoField(primary_key=True)
    stock_name = models.CharField(unique=True, max_length=20)

    class Meta:
        db_table = 'stock_list'
