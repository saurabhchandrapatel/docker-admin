
from .admin import CommonAdmin , admin
#from virtualization.forms import VolumesFrom
from virtualization.models import Volumes

@admin.register(Volumes)  
class VolumesAdmin(CommonAdmin):
    """docstring for Images"""
    #form = VolumesFrom
    list_display = ("name","volume_id",) 
    search_fields = ("name" , "volume_id")
        