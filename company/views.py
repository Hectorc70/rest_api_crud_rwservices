from django.shortcuts import render


from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404



from .models import Company, Area

from .models import (Activity, Picture,
                    Task)

from .serializers import CompanySerializer, AreaSerializer
from .serializers import (ActivitySerializer, PictureSerializer,
                            TaskSerializer)

class CompanyRecordView(APIView):
    #permission_classes = [IsAdminUser]
    def get(self, request, company):
        companys = Company.objects.filter(rfc=company)
        serializer = CompanySerializer(companys, many=True)

        return Response(serializer.data)

    
    def post(self, request, format=None):
        serializer = CompanySerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data, 
                            status= status.HTTP_201_CREATED)

        return Response(serializer.errors, 
                            status= status.HTTP_400_BAD_REQUEST)
class AreaRecordView(APIView):
    def get(self, request,company):

        areas_company = Area.objects.filter(company=company)
        serializer = AreaSerializer(areas_company, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AreaSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data, 
                            status= status.HTTP_201_CREATED)

        return Response(serializer.errors, 
                            status= status.HTTP_400_BAD_REQUEST)


class ActivitysAreaRecordView(APIView):
    def get(self, request, area):


        activities_area = Activity.objects.filter(area=area)
        serializer = ActivitySerializer(activities_area, many=True)

        return Response(serializer.data)

class ActivitysUserRecordView(APIView):
    def get(self, request, user):
        activities_area = Activity.objects.filter(created_by = user)
        serializer = ActivitySerializer(activities_area, many=True)
        return Response(serializer.data)

class ActivityRecordView(APIView):
    def get(self, request, id_activity):

        activity = Activity.objects.filter(id_activity=id_activity)
        serializer_activity = ActivitySerializer(activity, many=True)       
        return Response(serializer_activity.data)

    def post(self, request, format=None):
        serializer = ActivitySerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data, 
                            status= status.HTTP_201_CREATED)

        return Response(serializer.errors, 
                            status= status.HTTP_400_BAD_REQUEST)

class PictureRecordView(APIView):
    def get(self, request, id_activity):        

        pictures = Picture.objects.filter(activity=id_activity)   
        serializer_pictures = PictureSerializer(pictures, many=True)



        return Response(serializer_pictures.data)

    def post(self, request, format=None):
        serializer = PictureSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data, 
                            status= status.HTTP_201_CREATED)

        return Response(serializer.errors, 
                            status= status.HTTP_400_BAD_REQUEST)

class TaskRecordView(APIView):
    def get(self, request, id_activity):        
        serializer_tasks = Task.objects.filter(activity=id_activity)
        serializer_tasks = TaskSerializer(serializer_tasks, many=True)
        return Response(serializer_tasks.data)



    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data, 
                            status= status.HTTP_201_CREATED)

        return Response(serializer.errors, 
                            status= status.HTTP_400_BAD_REQUEST)
