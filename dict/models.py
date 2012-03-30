from django.db import models

class Host(models.Model):
    name = models.CharField(max_length=128)
    ip = models.CharField(max_length=15)
    ops_contacter = models.CharField(max_length=64)
    os_info = models.CharField(max_length=64)
    gmt_created = models.DateTimeField('date published')
    gmt_modified = models.DateTimeField('date modified')
    comment = models.CharField(max_length=256)

class Instance(models.Model):
    host_id = models.IntegerField()
    name = models.CharField(max_length=128)
    dba_contacter = models.CharField(max_length=64)
    version = models.DecimalField(max_digits=5, decimal_places=2)
    version_comment = models.CharField(max_length=64)
    gmt_created = models.DateTimeField('date published')
    gmt_modified = models.DateTimeField('date modified')
    comment = models.CharField(max_length=256)

class Database(models.Model):
    instance_id = models.IntegerField()
    name = models.CharField(max_length=123)
    gmt_created = models.DateTimeField('date published')
    gmt_modified = models.DateTimeField('date modified')
    comment = models.CharField(max_length=256)
