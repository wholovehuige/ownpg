from __future__ import unicode_literals
from django.db import models

# Create your models here.

class dbMessage(models.Model):
    ip_address = models.CharField(max_length=32,default='')
    port = models.CharField(max_length=32 , default='')
    db_name = models.CharField(max_length=128,default='')
    username = models.CharField(max_length=128,default='')
    password = models.CharField(max_length=128,default='')

    def __str__(self):
        return self.ip_address

class topTable(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=32 , default='')
    table_name = models.CharField(max_length=32 , default='')
    search_value = models.CharField(max_length=128, default='')
    search_type = models.CharField(max_length=8 , default='')
    search_type_name = models.CharField(max_length=32 , default='')
    isUse = models.CharField(max_length=8,default='0')
    relation = models.CharField(max_length=128,default='')

    def __str__(self):
        return self.name

class relationTable(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    topName = models.CharField(max_length=32,default='')
    topId = models.BigIntegerField
    ralation_field = models.CharField(max_length=32,default='')
    search_col = models.CharField(max_length=32,default='')