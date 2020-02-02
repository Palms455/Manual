from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Schedule, Element
from .serializers import ScheduleSerializer, ElementSerializer
from datetime import datetime
from rest_framework.pagination import PageNumberPagination
from .utils import PaginateMixin, ValidateData
# Create your views here.

class BasicPagination(PageNumberPagination):
    page_size_query_param = 'limit'


class ScheduleView(PaginateMixin, APIView):
	pagination_class = BasicPagination
	serializer_class = ScheduleSerializer

	def get(self, request):
		in_date = request.GET.get("date")
		if in_date:
			try:
				in_date = datetime.strptime(in_date, '%Y-%m-%d')
			except:
				return Response({'Введите корректный формат даты. YYYY-MM-DD'})

			schedules = Schedule.objects.exclude(date__lte=in_date)
			if schedules:
				return self.paginate_run(obj=schedules)

			return Response({f"Schedules does not exist on '{in_date}' " })

		schedules = Schedule.objects.all()
		return self.paginate_run(obj=schedules)
		


class ElementView(PaginateMixin, APIView):

	pagination_class = BasicPagination
	serializer_class = ElementSerializer

	def get(self, request):
		in_schedule = request.GET.get('schedule')
		in_version = request.GET.get('version', '')
		if not in_schedule:
			content = {"schedule": ["This field may not be blank."]}
			return Response(content, status=status.HTTP_400_BAD_REQUEST)
		if in_version:
			try:
				item = Schedule.objects.get(version = in_version)
			except Schedule.DoesNotExist:
				return Response({'Version does not exist'})
				
			elements = Element.objects.filter(schedule=item)
			return self.paginate_run(obj=elements)
		try:
			item = Schedule.objects.filter(title=in_schedule).order_by('-version').first()
		except Schedule.DoesNotExist:
			return Response({'Schedule does not exist'})

		elements = Element.objects.filter(schedule=item)
		return self.paginate_run(obj=elements)

		

class ValidateElementView(APIView, ValidateData):

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
			return self.validate_element(in_code, in_value)

		try:
			item = Schedule.objects.get(title=in_schedule, version=in_version)
		except Schedule.DoesNotExist:
			return Response(content, status=status.HTTP_404_NOT_FOUND)
		return self.validate_element(in_code, in_value, item)

	def validate_element(self, in_code, in_value, item):
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