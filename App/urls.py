from . import views
from django.urls import path

urlpatterns = [
	path('read/',views.read),
	path('add/',views.add),
	path('delete/',views.delete)
]