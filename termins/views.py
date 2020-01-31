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

		

class ValidateElementView(APIView):
	def get(self,request):
		in_version = request.GET.get('version')
		in_schedule = request.GET.get('schedule')
		in_code = request.GET.get('code')
		in_value = request.GET.get('value')

		if not in_schedule:
			content = {"schedule": ["This field may not be blank."]}
			return Response(content, status=status.HTTP_400_BAD_REQUEST)
		item = Schedule.objects.filter(title = in_schedule)
		if not item:
			content={f'{in_schedule} does not exist'}
			return Response(content, status=status.HTTP_404_NOT_FOUND)
		if not in_version:
			item = Schedule.objects.filter(title=in_schedule).order_by('-version').first()
			if not in_code:
				content = {"code": ["This field may not be blank."]}
				return Response(content, status=status.HTTP_400_BAD_REQUEST)
			if not in_value:
				content = {"value": ["This field may not be blank."]}
				return Response(content, status=status.HTTP_400_BAD_REQUEST)
			try:
				element = Element.objects.get(code=in_code, schedule=item)
			except Element.DoesNotExist:
				content={f'{in_code} does not exist'}
				return Response(content, status=status.HTTP_404_NOT_FOUND)
			if element.value != in_value:
				content={f'{in_value} does not equal {element.value}'}
				return Response(content, status=status.HTTP_404_NOT_FOUND)
			else:
				return Response({"all checked!!!"})

		try:
			item = Schedule.objects.get(title=in_schedule, version=in_version)
		except Schedule.DoesNotExist:
			return Response(content, status=status.HTTP_404_NOT_FOUND)
		if not in_code:
			content = {"code": ["This field may not be blank."]}
			return Response(content, status=status.HTTP_400_BAD_REQUEST)
		if not in_value:
			content = {"value": ["This field may not be blank."]}
			return Response(content, status=status.HTTP_400_BAD_REQUEST)
		try:
			element = Element.objects.get(code=in_code, schedule=item)
		except Element.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND, content={f'{in_code} does not exist'})
		if element.value != in_value:
			return Response(status=status.HTTP_404_NOT_FOUND, content={f'{in_value} does not equal {element.value}'})
