
from .admin import CommonAdmin , admin
from virtualization.models import Volumes

@admin.register(Volumes)  
class VolumesAdmin(CommonAdmin):
    """docstring for Images"""
    ...
        