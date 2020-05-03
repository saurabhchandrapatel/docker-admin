
from .admin import CommonAdmin , admin
from virtualization.models import Services
#from virtualization.forms import ServicesFrom

@admin.register(Services)
class ServicesAdmin(CommonAdmin):
    """docstring for Images"""
    #form = ServicesFrom
    list_display = ("name","version",) 
    search_fields = ("name" , "version")
    