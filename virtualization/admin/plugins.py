
from .admin import CommonAdmin , admin
from virtualization.models import Plugins

@admin.register(Plugins)
class PluginsAdmin(CommonAdmin):
    """docstring for Images"""
    ...