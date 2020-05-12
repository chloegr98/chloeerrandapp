from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ErrandSerializer

from .models import Errand
# Create your views here.

# Decorator + response allows us to have the functionality django rest framework gives us
@api_view(['GET'])
def api(request):
    #urls that user will see if they want to view the api
    api_urls = {
        'Summary' : '/errand-summary/',
        'Information' : '/errand-info/<str:pk>/',
        'Create' : '/errand-create/',
        'Update' : '/errand-update/<str:pk>/',
        'Delete' : '/errand-delete/<str:pk>/',
    }

    return Response(api_urls)


# view that queries all tasks from databases, thrown into serializer, serializes data and returns it in our api response
# only want to allow a get call
@api_view(['GET'])
def errandSummary(request):
    errands = Errand.objects.all()
    errandSerializer = ErrandSerializer(errands, many=True)
    return Response(errandSerializer.data)

#only returns one errand object
@api_view(['GET'])
def errandInfo(request, pk):
    errand = Errand.objects.get(id=pk)
    errandSerializer = ErrandSerializer(errand, many=False)
    return Response(errandSerializer.data)


#creates a new errand
#only allows a post method
@api_view(['POST'])
def errandCreate(request):
    errandSerializer = ErrandSerializer(data=request.data)

    #if it's valid it sends it back to the database and saves it
    if errandSerializer.is_valid():
        errandSerializer.save()

    return Response(errandSerializer.data)

    
#updates an existing errand
#only allows a post method
@api_view(['POST'])
def errandUpdate(request, pk):
    errand = Errand.objects.get(id=pk)
    errandSerializer = ErrandSerializer(instance=errand, data=request.data)

    #if it's valid it sends it back to the database and saves it
    if errandSerializer.is_valid():
        errandSerializer.save()

    return Response(errandSerializer.data)

#deletes an existing errand
#uses a delete method
@api_view(['DELETE'])
def errandDelete(request, pk):
    errand = Errand.objects.get(id=pk)
    errand.delete()

    return Response("Errand Deleted.")