from django.forms import forms, ModelForm
from .models import *

class ChatForm(ModelForm):
    class Meta:
        model = GroupMessage
        fields = '__all__'