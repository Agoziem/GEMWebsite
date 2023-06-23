from django.shortcuts import render,redirect
from .models import *
from Articles.models import Articles
# from Blog.models import Article
# from .forms import Contactform
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse
import json


def home_view(request):
	queryset1=Organization_detail.objects.get(id=1)
	first_three_Project = Project.objects.all()[:3]
	second_three_Project= Project.objects.all()[3:6]
	queryset4=Staff.objects.all()
	queryset5=Event.objects.order_by('-id')[:3]
	Main_event=Event.objects.order_by('-id')[:1]
	queryset6=Photo.objects.order_by('-id')[:6]
	# queryset7=Teacher.objects.all()
	# queryset8=ParentsReview.objects.all()
	queryset9=Articles.objects.order_by('-id')[:3]
	context= {
	# 'mapbox_private_key':settings.MAPBOXGL_ACCESSTOKEN,
	'GEM':queryset1,
	'first_three_Project':first_three_Project,
    "second_three_Project":second_three_Project,
	# 'headers':queryset3,
	'Staffs':queryset4,
	"Main_event":Main_event,
	'events':queryset5,
	'photos':queryset6,
	# "Teachers":queryset7,
	# "parentsreviews":queryset8,
	"articles":queryset9
	}
	return render(request,'home.html',context)

def photo_gallery_view(request):
	Pictures=Photo.objects.all()
	context={
		"Pictures":Pictures
	}
	return render(request,'photogallery.html',context)

def about_view(request):
	queryset1=Organization_detail.objects.get(id=1)
	queryset4=Staff.objects.all()
	context={
		"GEM":queryset1,
		"Staffs":queryset4
	}
	return render(request,'about.html',context)

def submit_contact_form(request):
    data=json.loads(request.body)
    contactname=data['userformdata']['name']
    contactemail=data['userformdata']['email']
    contactmessage=data['userformdata']['message']
    contact_info=Contact.objects.create(
        name=contactname,
        email=contactemail,
        message=contactmessage
    )
    contact_info.save()

    return JsonResponse('submitted successfully',safe=False)

def submit_sub_form(request):
    data=json.loads(request.body)
    subemail=data['userdata']['email']
    sub_email=Subscription.objects.create(Email=subemail)
    sub_email.save()
    return JsonResponse('submitted successfully',safe=False)
