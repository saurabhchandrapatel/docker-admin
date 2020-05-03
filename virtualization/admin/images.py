
from .admin import CommonAdmin , admin
from virtualization.models import Images


@admin.register(Images)
class ImagesAdmin(CommonAdmin):
    """docstring for Images"""
    ...