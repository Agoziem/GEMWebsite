from django.urls import path
from .views import *

app_name = 'Payment'
urlpatterns = [
	path('',initiate_payment,name='initiate'),
    path('success/<str:ref>/', successMsg, name="success"),
    ]