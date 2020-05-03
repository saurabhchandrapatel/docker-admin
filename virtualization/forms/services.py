from .forms import Form
from virtualization.models import Services

class ServicesForm(models.Model):
    """docstring for Images"""
    class Meta:
        model = Services
        fields = __all__