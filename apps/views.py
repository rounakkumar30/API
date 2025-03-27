# apps/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import App
from .serializers import AppSerializer

@api_view(['POST'])
def add_app(request):
    serializer = AppSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_app(request, id):
    try:
        app = App.objects.get(pk=id)
        serializer = AppSerializer(app)
        return Response(serializer.data)
    except App.DoesNotExist:
        return Response({'error': 'App not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_app(request, id):
    try:
        app = App.objects.get(pk=id)
        app.delete()
        return Response({'message': 'App deleted successfully'})
    except App.DoesNotExist:
        return Response({'error': 'App not found'}, status=status.HTTP_404_NOT_FOUND)

# apps/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')
