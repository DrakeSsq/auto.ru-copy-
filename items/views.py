from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .forms import *

# Create your views here.

def index(request, slug1=None, slug2=None, slug3=None, slug4=None):


    if slug1 == 'add_item' and slug2==None:
        data = {
            'type': Transport.objects.all(),
        }
        return render(request, 'add_item.html', data)
    
    if slug2 == 'legkovie-avtomobili' and slug3==None:
        data = {
            'marka': Marka_Legkovoe_Avto.objects.all(),
            'model': Model_Legkovoe_Avto.objects.all(),
        }
        return render(request, 'add_item_legkovoe_avto.html', data)
    

    
    if slug4 and slug1 == 'add_item':
        model = get_object_or_404(Model_Legkovoe_Avto, slug=slug4)
        marka = model.parent
        type = marka.parent


        if request.method == 'POST':
            form_item = Add_Legkovoe_Avto(request.POST, request.FILES)
            form_image = Add_Image_Legkovoe_Avto(request.POST, request.FILES)
            if form_item.is_valid() and form_image.is_valid():
                form = form_item.save()
                for files in request.FILES.getlist('images'):
                    Image_Legkovoe_Avto.objects.create(avto=form, images=files)
                return redirect('home')


        else:
            form_item = Add_Legkovoe_Avto(initial={'marka': marka, 'parent': model, 'type':type})
            form_image = Add_Image_Legkovoe_Avto()

        data = {'form_item': form_item, 'form_image': form_image, 'marka':marka, 'model': model, 'type':type}

        
        return render(request, 'add_form_legkovoe_avto.html', data)
    
    return render(request, 'index.html')


def context(request): pass 