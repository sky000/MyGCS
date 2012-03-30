from django.shortcuts import render_to_response
from dict.models import Host,Instance,Database


def left_tree_show():
    host_list = Host.objects.all().order_by('gmt_created')
    list = []
    uid = 0
    for h in host_list:
        uid = uid + 1
        host = {}
        host['id'] = h.id 
        host['name'] = h.name
        host['gmt_created'] = h.gmt_created
        host['gmt_modified'] = h.gmt_modified
        host['comment'] = h.comment
        host['tid'] = uid
        host['pid'] = 0
        host['type'] = 'host'
        list.append(host)
        
        instace_list = Instance.objects.filter(host_id = h.id)
        for i in instace_list:
            uid = uid + 1
            instance = {}
            instance['id'] = i.id 
            instance['name'] = i.name
            instance['gmt_created'] = i.gmt_created
            instance['gmt_modified'] = i.gmt_modified
            instance['comment'] = i.comment
            instance['tid'] = uid
            instance['pid'] = host['tid']
            instance['type'] = 'instance'
            list.append(instance);
            
            database_list = Database.objects.filter(instance_id = i.id)
            for d in database_list:
                uid = uid + 1
                db = {}
                db['id'] = d.id 
                db['name'] = d.name
                db['gmt_created'] = d.gmt_created
                db['gmt_modified'] = d.gmt_modified
                db['comment'] = d.comment
                db['tid'] = uid
                db['pid'] = instance['tid']
                db['type'] = 'database'
                list.append(db);

    return list
    
    
