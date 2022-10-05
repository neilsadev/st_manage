import uuid
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser

from .models import Student
from .serializers import StudentSerializer

#Create and Read Institutes
@api_view(['GET', 'POST'])
def student_list(request, format=None):

    if request.method == 'GET':
        #fetch object
        students = Student.objects.all()
        #serialize
        serializer = StudentSerializer(students, many=True)
        #return Response
        return Response({"students": serializer.data}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        #fetch data
        insData = JSONParser().parse(request)
        serializer = StudentSerializer(data=insData)
        print(serializer)
        if serializer.is_valid():
            #if valid deserialize and save
            serializer.save()
            # return response
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors,
                            status=400)

#Read, Update and Delete Institues by uuid
@api_view(['GET', 'PUT', 'DELETE'])
def sstudent_detail_by_uid(request, id, format=None):
    #fetch data
    try:
        institute = Student.objects.get(uuid = id)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        #serialize
        serializer = StudentSerializer(institute)
        #reutn resposne
        return Response({"student": serializer.data}, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = StudentSerializer(institute, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"updated_student": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        institute.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)