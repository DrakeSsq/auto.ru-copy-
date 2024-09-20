from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from .forms import *
from django.contrib.auth.decorators import login_required
from .filters import *
from django.contrib.auth import get_user_model
from .models import *


def profile(request):
    if request.method == 'POST':
        form = ProfileUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = ProfileUserForm(instance=request.user)
    user = request.user
    return render(request, 'profile.html', {'user':user, 'form':form})

def index(request, slug1=None, slug2=None, slug3=None, slug4=None):





    
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
        
        

    if slug1 == 'legkovie-avtomobili':
        if slug2 and not slug3 and not slug4:


            car = Legkovoe_Avto.objects.filter(marka__slug=slug2)
            car_image = Image_Legkovoe_Avto.objects.all()

            model = Model_Legkovoe_Avto.objects.filter(parent__slug=slug2)
            marka = slug2

            filter = Legkovoe_Avto_Filter(request.GET, queryset=car)

            return render(request, 'views/avto/selected_marka.html', {'car':car, 'marka':marka, 'model':model, 'car_image':car_image, 'filter':filter})
        
        if slug2 and slug3 and not slug4:
            marka = slug2
            model = slug3
            car = Legkovoe_Avto.objects.filter(marka__slug=slug2, parent__slug=slug3)
            return render(request, 'views/avto/selected_model_all.html', {"car":car, 'marka':marka, 'model':model})
        
        if slug4:
            car = get_object_or_404(Legkovoe_Avto, slug=slug4)

            images = Image_Legkovoe_Avto.objects.filter(avto=car)

            return render(request, 'views/avto/item_avto.html', {"car":car, "images":images})
        
    
    data = {
        'title': 'Авто.ру',

        'avto': Legkovoe_Avto.objects.all(),
        'marka_legkovoe_avto': Marka_Legkovoe_Avto.objects.all(),
        'avto_image': Image_Legkovoe_Avto.objects.all(),

        'filter': Legkovoe_Avto_Filter(request.GET, queryset=Legkovoe_Avto.objects.all())
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

