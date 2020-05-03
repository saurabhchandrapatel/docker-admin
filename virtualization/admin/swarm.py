
from .admin import CommonAdmin , admin
from virtualization.models import Swarm
#from virtualization.forms import SwarmFrom

@admin.register(Swarm) 
class SwarmAdmin(CommonAdmin):
    """docstring for Images"""
    #form = SwarmFrom
    ...
    