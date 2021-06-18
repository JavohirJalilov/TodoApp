from . import views
from django.urls import path

urlpatterns = [
	path('read/',views.read)
]