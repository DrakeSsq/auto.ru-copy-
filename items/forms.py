from django import forms
from .models import *
from django.contrib.auth import get_user_model

class Add_Legkovoe_Avto(forms.ModelForm):
    class Meta:
        model = Legkovoe_Avto
        fields = '__all__'
        exclude = ('author', 'time_create', 'time_update',)

        widgets = {
            'marka': forms.HiddenInput(),
            'type': forms.HiddenInput(),
            'parent': forms.HiddenInput(),
        }

class Add_Image_Legkovoe_Avto(forms.ModelForm):
    class Meta:
        model = Image_Legkovoe_Avto
        fields = ('images',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['images'].widget.attrs['multiple'] = True


class ProfileUserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name']