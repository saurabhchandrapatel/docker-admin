
from .admin import CommonAdmin , admin
from virtualization.models import Containers
#from virtualization.forms import ContainersFrom


@admin.register(Containers)
class ContainersAdmin(CommonAdmin):

    #form = ContainersFrom
    list_display = ("labels", "attrs",)
    search_fields = ("name" , "labels")