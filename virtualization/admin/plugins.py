
from .admin import CommonAdmin , admin
from virtualization.models import Plugins
 
#from virtualization.forms import PluginsFrom

@admin.register(Plugins)
class PluginsAdmin(CommonAdmin):
    """docstring for Images"""
    #form = PluginsFrom
    list_display = ("name","attrs",) 
    search_fields = ("name" , "attrs")