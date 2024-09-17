from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from .forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib.auth import get_user_model

def index(request, slug1=None, slug2=None, slug3=None, slug4=None):

    # if slug1 == 'users':
    #     if slug2 == 'login': return redirect(reverse('users:login'))
    #     if slug2 == 'logout': return redirect(reverse('users:logout'))

    
    if slug1 == 'add_item':

        if slug2 == 'legkovie-avtomobili':

            if slug3 and not slug4:
                marka = get_object_or_404(Marka_Legkovoe_Avto, slug=slug3)
                marka_slug = marka.slug
                return add_avto_model(request, {"marka_slug":marka_slug})
            
            if slug4:
                model = get_object_or_404(Model_Legkovoe_Avto, slug=slug4)
                marka = model.parent
                type = marka.parent
                data = {
                    'model': model,
                    'marka': marka,
                    'type': type,
                }
                return add_avto_full(request, data)
            return add_avto_marka(request)
        

        if slug2 == 'mototechnika':
            return add_moto(request)
        
    
    data = {
        'title': 'Авто.ру',
        'avto': Legkovoe_Avto.objects.all(),
        'avto_image': Image_Legkovoe_Avto.objects.all(),
    }    
    
    return render(request, 'index.html', data)



@login_required(login_url='users:login')
def add_item(request):
    data = {
        'type': Transport.objects.all(),
    }
    return render(request, 'add/add_item.html', data)


def add_avto_marka(request):
    data = {
        'marka': Marka_Legkovoe_Avto.objects.all(),
    }
    return render(request, 'add/avto/add_avto_marka.html', data)


def add_avto_model(request, marka_slug=None):
    data = {
        'model': Model_Legkovoe_Avto.objects.filter(parent__slug=marka_slug.get('marka_slug')),
        
    }
    return render(request, 'add/avto/add_avto_model.html', data)

def add_avto_full(request, data):
    if request.method == 'POST':
        form_item = Add_Legkovoe_Avto(request.POST, request.FILES)
        form_image = Add_Image_Legkovoe_Avto(request.POST, request.FILES)
        if form_item.is_valid() and form_image.is_valid():
            form = form_item.save(commit=False)
            form.author = request.user
            form.save()
            for files in request.FILES.getlist('images'):
                Image_Legkovoe_Avto.objects.create(avto=form, images=files)
            return redirect('home')


    else:
        form_item = Add_Legkovoe_Avto(initial={'marka': data.get('marka'), 'parent': data.get('model'), 'type':data.get('type')})
        form_image = Add_Image_Legkovoe_Avto()

    data = {'form_item': form_item, 'form_image': form_image, 'marka': data.get('marka'), 'model':data.get('model'), 'type':data.get('type')}

    return render(request, 'add/avto/add_avto_full.html', data)



def add_moto(request):
    return HttpResponse('lol moto')

