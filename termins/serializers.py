from rest_framework import serializers
from .models import Schedule, Element
class ScheduleSerializer(serializers.ModelSerializer):

	class Meta:
		model = Schedule
		fields=('name', 'title', 'description', 'version', 'date')


class ElementSerializer(serializers.ModelSerializer):

	schedule = serializers.CharField(source="schedule.title", read_only=True)
	#show title instead shedule_id

	class Meta:
		model = Element
		fields = ('schedule', 'code', 'value')
	
	
