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
	queryset2=Project.objects.all()
	# queryset3=Header.objects.all()
	queryset4=Staff.objects.all()
	queryset5=Event.objects.order_by('-id')[:2]
	Main_event=Event.objects.order_by('-id')[:1]
	queryset6=Photo.objects.order_by('-id')[:6]
	# queryset7=Teacher.objects.all()
	# queryset8=ParentsReview.objects.all()
	queryset9=Articles.objects.order_by('-id')[:3]
	context= {
	# 'mapbox_private_key':settings.MAPBOXGL_ACCESSTOKEN,
	'GEM':queryset1,
	'projects':queryset2,
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
