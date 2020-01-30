from django.db import models

# Create your models here.
class Schedule(models.Model):
	name = models.CharField(max_length=250)
	title = models.CharField(max_length=150)
	description = models.TextField(blank=True)
	version = models.CharField(unique=True, max_length=250)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title


class Element(models.Model):
	schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
	code = models.CharField(max_length=250)
	value = models.CharField(max_length=250)

	def __str__(self):
		return self.code

