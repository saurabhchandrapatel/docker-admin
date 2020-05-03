
from .admin import CommonAdmin , admin
from virtualization.models import Secrets



@admin.register(Secrets)
class SecretsAdmin(CommonAdmin):
    """docstring for Images"""
    ...