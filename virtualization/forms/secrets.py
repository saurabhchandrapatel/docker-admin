
from .forms import Form
from virtualization.models import Secrets



class SecretsForm(models.Model):
    """docstring for Images"""
    class Meta:
        model = Secrets
        fields = __all__