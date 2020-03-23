from rest_framework import serializers
from .models import Module,Professor,RateInfo,Results

class ModuleSerializers(serializers.ModelSerializer):
 class Meta:
     model = Module
     fields = ('Code','Name','Year','Semester','Taught_by')
class Result2Serializers(serializers.ModelSerializer):
 class Meta:
     model = Results
     fields = ('Name','Rate')
class RateSerializers(serializers.ModelSerializer):
 class Meta:
     model= RateInfo
     fields = ('Name','Professor','Rate')