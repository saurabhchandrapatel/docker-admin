
from .admin import CommonAdmin , admin
from virtualization.models import Configs

@admin.register(Configs)
class ConfigsAdmin(CommonAdmin):
    ...
    
    
