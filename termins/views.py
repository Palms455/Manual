from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Schedule, Element
# Create your views here.


class ScheduleView(APIView):
	def get(self, request):
		list_schedule = Schedule.objects.all()
		return Response({'list_schedule' : list_schedule})

class ElementView(APIView):
	def get(self, request):
		list_elements = Element.objects.all()
		return Response({'list_elements' : list_elemetns})

