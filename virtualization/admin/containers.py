
from .admin import CommonAdmin , admin
from virtualization.models import Containers


@admin.register(Containers)
class ContainersAdmin(CommonAdmin):
    """docstring for Images"""
    ...