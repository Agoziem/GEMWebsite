from django.shortcuts import render,redirect
from .models import *
from django.urls import reverse
from django.http import JsonResponse
# from django.conf import settings
# import stripe

# stripe.api_key = settings.STRIPE_SECRET_KEY
# Create your views here.

def initiate_payment(request):
	if request.method == 'POST':
		Name = request.POST['Name']
		email = request.POST['email']
		Amount = request.POST['Amount']
		description = request.POST['description']
		Partnership_type = request.POST['Partnership_type']

		payment=Donations_and_Support(Name=Name,Payment_description=description,Partnership_type=Partnership_type, Email=email,total_amount=Amount,verified=False)
		payment.save()
		context={
			"Payment":payment
		}
		return render(request, 'make_payment.html',context)

	return render(request, 'initiate_payment.html')



def successMsg(request, ref):
	Payment=Donations_and_Support.objects.get(ref=ref)
	Payment.verified = True
	Payment.save()
	print(Payment.ref)
	context={
		"payment":Payment
	}
	return render(request, 'Successful.html', context)