
from .admin import CommonAdmin , admin
from virtualization.models import Secrets
#from virtualization.forms import SecretsFrom


@admin.register(Secrets)
class SecretsAdmin(CommonAdmin):
    """docstring for Images"""
    #form = SecretsFrom
    list_display = ("name","attrs",) 
    search_fields = ("name" , "attrs")