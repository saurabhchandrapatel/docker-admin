
from .admin import CommonAdmin , admin
from virtualization.models import Images
#from virtualization.forms import ImagesFrom


@admin.register(Images)
class ImagesAdmin(CommonAdmin):
    #form = ImagesFrom
    list_display = ("name", "labels","attrs", "tags") 
    search_fields = ("name" , "labels")
