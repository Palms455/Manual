from django.urls import path
from .views import ScheduleView, ElementView,  ValidateElementView

app_name = 'schedules'

urlpatterns = [
	path('schedules/', ScheduleView.as_view()),
	path('elements/', ElementView.as_view()),
	path('validate/', ValidateElementView.as_view()),

]

