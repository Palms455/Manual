from django.urls import path
from .views import ScheduleView, ElementView,  ElementsVersionView, ValidateElementView

app_name = 'schedules'

urlpatterns = [
	path('schedules/', ScheduleView.as_view()),
	path('elements/', ElementView.as_view()),
	path('elements/<str:in_version>/', ElementsVersionView.as_view()),
	path('validate/', ValidateElementView.as_view())

]

