from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Schedule, Element
from .serializers import ScheduleSerializer, ElementSerializer
from dateutil import parser
# Create your views here.


class ScheduleView(APIView):
	def get(self, request):
		in_date= request.GET.get("date", "")
		if in_date:
			try:
				in_date = utils.get_date(row_date)
			except:
				return Response({'Введите корректный формат даты. YYYY - MM - DD, или MM-DD - за этот год '})	
			schedules = Schedule.objects.exclude(date__lte=in_date)
			if schedules:
				serializer = ScheduleSerializer(schedules, many=True)
				return Response({'schedules' : serializer.data})
			return Response({f"Schedules does not exist on '{in_date}' " })

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


class ElementView(APIView):
	def get(self, request):
		in_schedule = request.GET.get('schedule')
		in_version = request.GET.get('version', '')
		if not in_schedule:
			content = {"schedule": ["This field may not be blank."]}
			return Response(content, status=status.HTTP_400_BAD_REQUEST)
		if in_version:
			try:
				item = Schedule.objects.get(version = in_version)
				elements = Element.objects.filter(schedule=item)
			except Schedule.DoesNotExist:
				return Response({'Version does not exist'})
			serializer = ElementSerializer(elements, many=True)
			return Response({'elements' : serializer.data})
		item = Schedule.objects.filter(title=in_schedule).order_by('-version').first()
		elements = Element.objects.filter(schedule=item)
		serializer = ElementSerializer(elements, many=True)
		return Response({'elements' : serializer.data})

		
class ElementsVersionView(APIView):
	def get(self, request, in_version):
 		elements = Element.objects.filter(schedule__version= in_version)
 		if elements:
 			serializer = ElementSerializer(elements, many=True)
 			return Response({'elements' : serializer.data})
 		return Response({'Does Not Exist'})

class ValidateElementView(APIView):
	def get(self,request):
		version = request.GET.get('version')
		in_schedule = request.GET.get('schedule')
		in_code = request.GET.get('code')
		in_value = request.GET.get('value')

