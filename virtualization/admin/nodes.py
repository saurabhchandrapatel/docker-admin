
from .admin import CommonAdmin , admin
from virtualization.models import Nodes

@admin.register(Nodes)
class NodesAdmin(CommonAdmin):
    ...