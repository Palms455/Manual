from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Schedule, Element
from .serializers import ScheduleSerializer, ElementSerializer
from dateutil import parser
# Create your views here.


class ScheduleView(APIView):
	def get(self, request):
		schedules = Schedule.objects.all()
		serializer = ScheduleSerializer(schedules, many=True)
		 # the many param informs the serializer that it will be serializing
		 # more than a single schedule.
		return Response({'schedules' : serializer.data})

	def post(self, request):
		schedule = request.data.get('schedule')
		# Create schedule from the above data
		serializer = ScheduleSerializer(data=schedule)
		if serializer.is_valid(raise_exception=True):
			new_schedule = serializer.save()
		return Response({f"success": "Schedule '{new_schedule.title}' created successfully"})

class ScheduleDateView(APIView):
	def get(self, request, row_date):
		in_date = parser.parse(row_date)
		schedules = Schedule.objects.exclude(date__lte=in_date)
		if schedules:
			serializer = ScheduleSerializer(schedules, many=True)
			return Response({'schedules' : serializer.data})
		return Response({f"Schedules does not exist on '{in_date}' " })

class ElementView(APIView):
	def get(self, request):
		elements = Element.objects.filter()
		serializer = ElementSerializer(elements, many=True)
		return Response({'elements' : serializer.data})

	def post(self, request):
		element = request.data.get('element')
		serializer = ElementSerializer(data = element)
		if serializer.is_valid(raise_exception=True):
			new_element = element.save()
		return Response({f"success": "Element '{new_element.title}' created successfully"})

class ElementsVersionView(APIView):
	def get(self, request, in_version):
 		elements = Element.objects.filter(schedule__version= in_version)
 		if elements:
 			serializer = ElementSerializer(elements, many=True)
 			return Response({'elements' : serializer.data})
 		return Response({'Does Not Exist'})
