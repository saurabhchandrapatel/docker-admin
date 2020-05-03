from .forms import Form
from virtualization.models import Images


class ImagesFrom(Form):
    class Meta:
        model = Images
        fields = '__all__'