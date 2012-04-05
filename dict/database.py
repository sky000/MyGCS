from django.shortcuts import render_to_response,get_object_or_404
from dict.models import *

def detail(request,database_id):
    d = get_object_or_404(Database, pk=database_id)
    i = get_object_or_404(Instance, pk=d.instance_id)
    h = get_object_or_404(Host, pk=i.host_id)
    navis = [];
    navis.append({'href':'/sys/host/'+str(h.id),'name':h.name})
    navis.append({'href':'/sys/instance/'+str(i.id),'name':i.name})
    navis.append({'href':'/sys/database/'+str(d.id),'name':d.name})
    
    return render_to_response('dict_database_detail.html', {'navis': navis, 'instance':i,'host': h,'database': d})