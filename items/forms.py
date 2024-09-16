from django import forms
from .models import *


class Add_Legkovoe_Avto(forms.ModelForm):
    class Meta:
        model = Legkovoe_Avto
        fields = '__all__'

class Add_Image_Legkovoe_Avto(forms.ModelForm):
    class Meta:
        model = Image_Legkovoe_Avto
        fields = ('images',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['images'].widget.attrs['multiple'] = True