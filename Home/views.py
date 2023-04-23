from django.shortcuts import render,redirect
from .models import *
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
	# queryset2=Management.objects.all()
	# queryset3=Header.objects.all()
	# queryset4=FAQ.objects.all()
	# queryset5=UpcomingEvents.objects.order_by('-id')[:2]
	# queryset6=PhotoGallery.objects.order_by('-id')[:6]
	# queryset7=Teacher.objects.all()
	# queryset8=ParentsReview.objects.all()
	# queryset9=Article.objects.order_by('-id')[:4]
	context= {
	# 'mapbox_private_key':settings.MAPBOXGL_ACCESSTOKEN,
	'GEM':queryset1,
	# 'managements':queryset2,
	# 'headers':queryset3,
	# 'FAQ':queryset4,
	# 'events':queryset5,
	# 'photos':queryset6,
	# "Teachers":queryset7,
	# "parentsreviews":queryset8,
	# "articles":queryset9
	}
	return render(request,'home.html',context)