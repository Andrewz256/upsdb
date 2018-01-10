import datetime


from django.db import models
from django.utils import timezone

# Create your models here.

class State(models.Model):
	stateUB=models.CharField(max_length=20,unique=True, null=False,blank=False)
	
	def __str__(self):
		return self.stateUB

class Modbat(models.Model):
	modBat=models.CharField(max_length=20,unique=True, null=False,blank=False)
	
	def __str__(self):
		return self.modBat

class Modups(models.Model):
	modUps=models.CharField(max_length=20,unique=True, null=False,blank=False)
	
	def __str__(self):
		return self.modUps

class Battery(models.Model):
	modBat = models.ForeignKey(Modbat,related_name="+",to_field="modBat", on_delete=models.SET_NULL,null=True)
	obitBN = models.CharField(max_length=20,primary_key=True,null=False)
	state = models.ForeignKey(State,related_name="+",to_field="stateUB", on_delete=models.SET_NULL,null=True)
	dateB = models.DateTimeField(default=timezone.now)
	commentB = models.CharField(max_length=50,blank=False)
	
	def __str__(self):
		return self.obitBN
	def publishb(self):
		self.dateB = timezone.now()
		self.save()
	
class UPSB(models.Model):
	modUps = models.ForeignKey(Modups,related_name="+",to_field="modUps", on_delete=models.SET_NULL,null=True,blank=False)
	obitN = models.CharField(max_length=20,blank=False)
	obitInsBat1 = models.ForeignKey(Battery, related_name="+", on_delete=models.SET_NULL,null=True,blank=True)
	obitInsBat2 = models.ForeignKey(Battery, related_name="+", on_delete=models.SET_NULL,null=True,blank=True)
	obitOutBat1 = models.ForeignKey(Battery, related_name="+", on_delete=models.SET_NULL,null=True,blank=True)
	obitOutBat2 = models.ForeignKey(Battery, related_name="+", on_delete=models.SET_NULL,null=True,blank=True)
	state = models.ForeignKey(State, related_name="+", to_field="stateUB", on_delete=models.SET_NULL,null=True)
	released = models.BooleanField(default=False)
	dateU = models.DateTimeField(default=timezone.now)
	commentU = models.CharField(max_length=100,blank=False)
	
	def __str__(self):
                return self.obitN
	def publishu(self):
		self.dateU = timezone.now()
		self.save()

