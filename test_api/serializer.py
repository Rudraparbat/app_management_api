from rest_framework import serializers 
from .models import *
class Appserializer(serializers.ModelSerializer) :
    class Meta :
        model = AppDetails
        fields = '__all__'