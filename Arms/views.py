from django.shortcuts import render
from .models import *
from Home.models import *

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
    Bible_studies_event=Event.objects.get(GEM_Arm="Bible Studies")
    context={
        "arm":Bible_studies,
        "Bible_studies_event":Bible_studies_event,
    }
    return render(request,"Bible_Studies.html",context)

# GEM Revival Prayers
def Revival_Prayers_view(request):
    Revival_Prayers=Arm.objects.get(Arm='Revival Prayers')
    Revival_Prayers_event=Event.objects.get(GEM_Arm='Revival Prayers')
    context={
        "arm":Revival_Prayers,
        "Revival_Prayers_event":Revival_Prayers_event,
    }
    return render(request,"Revival_Prayers.html",context)

# GEM Women's Hub
def Womens_view(request):
    Women=Arm.objects.get(Arm='Women’s Hub')
    Women_event=Event.objects.get(GEM_Arm='Women’s Hub')
    context={
        "arm":Women,
        "Women_event":Women_event
    }
    return render(request,"Womens.html",context)

# GEM Foundations
def Foundation_view(request):
    Foundations=Arm.objects.get(Arm='Foundation')
    first_three_Project = Project.objects.all()[:3]
    second_three_Project= Project.objects.all()[3:6]
    # Foundation_event=Event.objects.get(GEM_Arm='Foundation')
    context={
        "arm":Foundations,
        'first_three_Project':first_three_Project,
        "second_three_Project":second_three_Project,
        # "Foundation_event":Foundation_event
    }
    return render(request,"Foundation.html",context)
