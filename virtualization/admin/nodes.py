
from .admin import CommonAdmin , admin
from virtualization.models import Nodes
#from virtualization.forms import NodesFrom

@admin.register(Nodes)
class NodesAdmin(CommonAdmin):
    
    #form = NodesFrom
    list_display = ("name","attrs",) 
    search_fields = ("name" , "attrs")