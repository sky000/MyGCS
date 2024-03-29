from django.shortcuts import render_to_response,get_object_or_404
from dict.models import *
from dict_tree import *
from dict_core import *



def list(request):
	hosts = Host.objects.all().order_by('name')
	return render_to_response('list_hosts.html',{'host_list':hosts})
	
def detail(request,host_id):
	myDict = MyDict('host')
	h = myDict.getHost(host_id)
	#h = get_object_or_404(Host, pk=host_id)
	navis = [];
	navis.append({'href':'/sys/host/'+str(host_id),'name':h.name})
	
	return render_to_response('dict_host_detail.html', {'navis': navis, 'host': h})

def update(request,host_id):
	h = request.POST
	return render_to_response('detail.html', {'host': h})
	
	
