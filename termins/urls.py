from django.urls import path
from .views import ScheduleView, ElementView, ScheduleDateView, ElementsVersionView

app_name = 'schedules'

urlpatterns = [
	path('schedules/', ScheduleView.as_view()),
	path('schedules/<str:row_date>/', ScheduleDateView.as_view()),
	path('elements/', ElementView.as_view()),
	path('elements/<str:in_version>/', ElementsVersionView.as_view()),

]

