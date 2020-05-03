
from .admin import CommonAdmin , admin
from virtualization.models import Configs
#from virtualization.forms import ConfigsFrom

@admin.register(Configs)
class ConfigsAdmin(CommonAdmin):
    
    #form = ConfigsFrom
    list_display = ("name", "attrs",)
    search_fields = ("name" , )

    
