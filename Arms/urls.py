from django.urls import path
from .views import *

app_name = 'Arms'
urlpatterns = [
	path('', Arms_view , name='arms'),
	path('<str:name>/details/',Arms_details_view, name='details'),
    # path('<str:classname>/post_attendance',post_attendance , name='post_attendance'),
    ]