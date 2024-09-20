from django.shortcuts import get_object_or_404, redirect, render

from chat.models import ChatGroup, GroupMessage
from .forms import *
from django.contrib.auth import get_user_model


# Create your views here.

def index(request):
    select_group = get_object_or_404(ChatGroup, group_name='main-group')
    messages = GroupMessage.objects.filter(group=select_group)
    
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.group = select_group
            form.author = request.user
            form.save()
            form = ChatForm()
            form.fields['group'].initial = select_group
            form.fields['author'].initial = request.user
    else:
        form = ChatForm()
        form.fields['group'].initial = select_group
        form.fields['author'].initial = request.user


    return render(request, 'test.html', {'select_group':select_group, 'messages':messages, 'form':form})
