
from .admin import CommonAdmin , admin
from virtualization.models import Networks
#from virtualization.forms import NetworksFrom


@admin.register(Networks)
class NetworksAdmin(CommonAdmin):
    """docstring for Images"""
    #form = NetworksFrom
    list_display = ("name","attrs",) 
    search_fields = ("name" , "attrs")