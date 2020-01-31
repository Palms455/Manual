from rest_framework import serializers
from .models import Schedule, Element
class ScheduleSerializer(serializers.Serializer):
	name = serializers.CharField(max_length=250)
	title = serializers.CharField(max_length = 150)
	description = serializers.CharField()
	version = serializers.CharField()
	date = serializers.CharField()

	def create(self, validated_data):
		return Schedule.objects.create(**validated_data)

class ElementSerializer(serializers.Serializer):
	schedule_id = serializers.IntegerField() 
	code = serializers.CharField()
	value = serializers.CharField()
	
