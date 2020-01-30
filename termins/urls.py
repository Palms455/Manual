from django.urls import path
from .views import ScheduleView

app_name = 'schedules'

urlpatterns = [
	path('schedules/', ScheduleView.as_view()),

]

