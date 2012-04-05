'''
Created on Apr 1, 2012

@author: sky
'''
from django.shortcuts import get_object_or_404
from dict.models import *

class MyDict(object):
    def __init__(self,type):
        self.type = type 
        
    def getHost(self,hid):
        
        return get_object_or_404(Host, pk=hid)
    
    def listHost(self):
        hlist = Host.objects.all().order_by('name')
        
        return hlist
    
    def saveHost(self,h):
        Host(h).save()
        
    def getInstance(self,iid):
        return get_object_or_404(Instance, pk=iid)
    
    def listInstance(self,hid):
        if hid == 0:
            ilist = Instance.objects.all().order_by('host_id','name')
        else:
            ilist = Instance.objects.filter(host_id = hid).order_by('name')
            
        return ilist
    
    def saveInstance(self,i):
        
        Instance(i).save()
        
    def getDatabase(self,did):
        return get_object_or_404(Database, pk=did)
    
    def listDatabase(self,iid):
        if iid == 0:
            dlist = Database.objects.all().order_by('host_id','instance_id','name')
        else:
            dlist = Database.objects.filter(instance_id = iid).order_by('name')
            
        return dlist
    
    def saveDatabase(self,d):
        
        Database(d).save()

