from django.forms import ModelForm
from .models import Merchandise

class MerchandiseForm(ModelForm):
    class Meta:
        model = Merchandise
        fields = ['mer_number','mer_name','mer_type']