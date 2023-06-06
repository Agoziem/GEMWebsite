from django.urls import path
from .views import *

app_name = 'Arms'
urlpatterns = [
	path('', Arms_view , name='arms'),
	path('Bible Studies/',Bible_Studies_view, name='Bible_Studies'),
    path('Revival Prayer/',Revival_Prayers_view, name='Revival_Prayer'),
    path('Womens Hub/',Womens_view, name='Womens_Hub'),
    path('Foundation/',Foundation_view, name='Foundations'),
    # path('<str:classname>/post_attendance',post_attendance , name='post_attendance'),
    ]