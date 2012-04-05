from django.shortcuts import render_to_response,get_object_or_404
from dict.models import *



def list(request,host_id):
    list = Instance.objects.filter(host_id=host_id).order_by('name')
    return render_to_response('list_instance.html',{'instance_list':list})
    
def detail(request,instance_id):
    i = get_object_or_404(Instance, pk=instance_id)
    h = get_object_or_404(Host, pk=i.host_id)
    navis = [];
    navis.append({'href':'/sys/host/'+str(i.host_id),'name':h.name})
    navis.append({'href':'/sys/instance/'+str(i.id),'name':i.name})
    
    return render_to_response('dict_instance_detail.html', {'navis': navis, 'instance':i,'host': h})

def update(request,host_id):
    h = request.POST
    return render_to_response('detail.html', {'host': h})
    
    
