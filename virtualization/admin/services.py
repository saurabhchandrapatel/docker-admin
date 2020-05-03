
from .admin import CommonAdmin , admin
from virtualization.models import Services

@admin.register(Services)
class ServicesAdmin(CommonAdmin):
    """docstring for Images"""

    ...
    