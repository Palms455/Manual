from django.contrib import admin
from .models import Schedule, Element
# Register your models here.
class ScheduleAdmin(admin.ModelAdmin):
	'''справочники'''
	list_display=('title','version','date')

class ElementAdmin(admin.ModelAdmin):
	list_display=('schedule', 'code', 'value')

admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Element, ElementAdmin)	