from django.shortcuts import render_to_response,get_object_or_404
from dict.dict_tree import *


def main(request):
    return render_to_response('setup_index.html',{'nodes':left_tree_show()})
    
    