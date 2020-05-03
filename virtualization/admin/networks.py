
from .admin import CommonAdmin , admin
from virtualization.models import Networks



@admin.register(Networks)
class NetworksAdmin(CommonAdmin):
    """docstring for Images"""
    ...