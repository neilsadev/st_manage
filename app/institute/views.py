import uuid
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Institute
from .serializers import InstituteSerializer

#Create and Read From API
@api_view(['GET', 'POST'])
def institute_list(request, format=None):

    if request.method == 'GET':
        #fetch object
        institues = Institute.objects.all()
        #serialize
        serializer = InstituteSerializer(institues, many=True)
        #return Response
        return Response({"institutes": serializer.data}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        #fetch data
        serializer = InstituteSerializer(data=request.data)
        if serializer.is_valid():
            #if valid deserialize and save
            serializer.save()
            # return response
            return Response(serializer.data, status=status.HTTP_201_CREATED)

#Read, Update and Delete by ID
@api_view(['GET', 'PUT', 'DELETE'])
def institute_detail(request, id, format=None):
    
    #fetch data
    try:
        institute = Institute.objects.get(pk=id)
    except Institute.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        #serialize
        serializer = InstituteSerializer(institute)
        #reutn resposne
        return Response({"institute": serializer.data}, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = InstituteSerializer(institute, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"updated_institute": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        institute.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Read, Update and Delete by uuid
@api_view(['GET', 'PUT', 'DELETE'])
def institute_detail_by_uid(request, id, format=None):
    #fetch data
    try:
        institute = Institute.objects.get(uuid = id)
    except Institute.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        #serialize
        serializer = InstituteSerializer(institute)
        #reutn resposne
        return Response({"institute": serializer.data}, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = InstituteSerializer(institute, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"updated_institute": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        institute.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)