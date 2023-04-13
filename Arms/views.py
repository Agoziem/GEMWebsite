from django.shortcuts import render
from .models import *

def Arms_views(request):
    arms=Arm.objects.order_by('-id')
    context={
        "arms":arms
    }
    return render(request,"Arms.html",context)

def Arms_details_view(request,name):
    arm=Arm.objects.get(Arm=name)
    context={
        "arm":arm
    }
    return render(request,"Arm_details.html",context)