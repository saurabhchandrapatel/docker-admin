
from .admin import CommonAdmin , admin
from virtualization.models import Swarm

@admin.register(Swarm) 
class SwarmAdmin(CommonAdmin):
    """docstring for Images"""
    ...