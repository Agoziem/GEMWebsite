from django.shortcuts import render
from .models import *

def Arms_view(request):
    arms=Arm.objects.order_by('-id')
    Bible_studies=Arm.objects.get(Arm="Bible Studies")
    Revival_Prayers=Arm.objects.get(Arm='Revival Prayers')
    Foundations=Arm.objects.get(Arm='Foundation')
    Women=Arm.objects.get(Arm='Women’s Hub')
    context={
        "arms":arms,
        "Bible_studies":Bible_studies,
        "Revival_Prayers":Revival_Prayers,
        "Foundations":Foundations,
        "Women":Women
    }
    return render(request,"Arms.html",context)

# GEM Bible Studies
def Bible_Studies_view(request):
    Bible_studies=Arm.objects.get(Arm="Bible Studies")
    context={
        "arm":Bible_studies
    }
    return render(request,"Bible_Studies.html",context)

# GEM Revival Prayers
def Revival_Prayers_view(request):
    Revival_Prayers=Arm.objects.get(Arm='Revival Prayers')
    context={
        "arm":Revival_Prayers
    }
    return render(request,"Revival_Prayers.html",context)

# GEM Women's Hub
def Womens_view(request):
    Women=Arm.objects.get(Arm='Women’s Hub')
    context={
        "arm":Women
    }
    return render(request,"Womens.html",context)

# GEM Foundations
def Foundation_view(request):
    Foundations=Arm.objects.get(Arm='Foundation')
    context={
        "arm":Foundations
    }
    return render(request,"Foundation.html",context)
