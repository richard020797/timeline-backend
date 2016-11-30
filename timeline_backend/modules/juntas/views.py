from .models import Junta
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import JuntaSerializer
from django.http import Http404

class ListJuntas(APIView):
	
	def get(self,request):
		juntas = Book.objects.all()
		serializer = JuntaSerializer(juntas, many=True)
		return Response(serializer.data)

	def post(self,request):
		serializer = JuntaSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(status=status.HTTP_201_CREATED)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)