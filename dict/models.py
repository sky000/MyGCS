from django.db import models

class Host(models.Model):
    name = models.CharField(max_length=128)
    ip = models.CharField(max_length=15)
    gmt_created = models.DateTimeField('date published')
    gmt_modified = models.DateTimeField('date modified')
    comment = models.CharField(max_length=256)

class Instance(models.Model):
    host_id = models.IntegerField()
    name = models.CharField(max_length=128)
    gmt_created = models.DateTimeField('date published')
    gmt_modified = models.DateTimeField('date modified')
    comment = models.CharField(max_length=256)

class Database(models.Model):
    instance_id = models.IntegerField()
    name = models.CharField(max_length=123)
    gmt_created = models.DateTimeField('date published')
    gmt_modified = models.DateTimeField('date modified')
    comment = models.CharField(max_length=256)
