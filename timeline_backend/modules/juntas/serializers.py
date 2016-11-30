from rest_framework import serializers
from .models import Junta

class JuntaSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Junta
