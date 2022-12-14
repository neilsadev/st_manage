import uuid
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser

from .models import Institute, Department
from .serializers import InstituteSerializer, DepartmentSerializer


#Create and Read Institutes
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
        insData = JSONParser().parse(request)
        serializer = InstituteSerializer(data=insData)
        if serializer.is_valid():
            #if valid deserialize and save
            serializer.save()
            # return response
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors,
                            status=400)


#Read, Update and Delete Institues by ID
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


#Read, Update and Delete Institues by uuid
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


#Get All Departments
@api_view(['GET',])
def department_list(request, format=None):

    if request.method == 'GET':
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response({"departments": serializer.data}, status=status.HTTP_200_OK)


#Attatch department with institute with uid
@api_view(['POST',])
def attatch_department_to_institute(request, id, format=None):
    #fetch data
    try:
        institute: Institute = Institute.objects.get(uuid = id)
    except Institute.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    print(institute)

    if request.method == 'POST':
        #fetch data
        depData: dict = JSONParser().parse(request)
        depData.update({"institute" : institute.id})
        print(depData)
        serializer = DepartmentSerializer(data=depData)
        if serializer.is_valid():
            #if valid deserialize and save
            serializer.save()
            # return response
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors,
                            status=400)


#get all departments in a institute
@api_view(['GET',])
def get_departments_by_institute(request, id, format=None):
    #fetch data
    try:
        queryInstitute = Institute.objects.get(uuid = id)
    except Institute.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    try:
        departments: list = Department.objects.filter(institute = queryInstitute.id)
    except Department.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        #serialize
        serializer = DepartmentSerializer(departments, many=True)
        #reutn resposne
        return Response({"institute": queryInstitute.name, "uuid": queryInstitute.uuid, "departments": serializer.data}, status=status.HTTP_200_OK)


#Update and Delete departmetns
@api_view(['PUT', 'DELETE',])
def department_actions(request, id, format=None):
    #fetch data
    try:
        department = Department.objects.get(id = id)
    except Department.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = DepartmentSerializer(department, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"updated_department": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        department.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
