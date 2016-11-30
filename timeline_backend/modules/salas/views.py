from .models import Sala
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SalaSerializer
from django.http import Http404

class ListAllSalas(APIView):
	
	def get(self,request):
		salas = Salas.objects.all()
		serializer = SalaSerializer(salas, many=True)
		return Response(serializer.data)
