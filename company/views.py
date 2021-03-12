from django.shortcuts import render


from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response



from .models import Company, Area

from .models import (Activity, PictureActivity,
                    Task)

from .serializers import CompanySerializer, AreaSerializer
from .serializers import (ActivitySerializer, PictureActSerializer,
                            TaskSerializer)

class CompanyRecordView(APIView):
    #permission_classes = [IsAdminUser]
    def get(self, request, company):
        companys = Company.objects.filter(rfc=company)
        serializer = CompanySerializer(companys, many=True)

        return Response(serializer.data)

class AreaRecordView(APIView):
    def get(self, request,company):

        areas_company = Area.objects.filter(company=company)
        serializer = AreaSerializer(areas_company, many=True)

        return Response(serializer.data)



class ActivitysAreaRecordView(APIView):
    def get(self, request, area):


        activities_area = Activity.objects.filter(area=area)
        serializer = ActivitySerializer(activities_area, many=True)

        return Response(serializer.data)

class ActivityRecordView(APIView):
    def get(self, request, id_activity):


        activity = Activity.objects.filter(id_activity=id_activity)   
        pictures = PictureActivity.objects.filter(activity=id_activity)   
        tasks = Task.objects.filter(activity=id_activity)  



        serializer_activity = ActivitySerializer(activity, many=True)
        serializer_pictures = PictureActSerializer(pictures, many=True)
        serializer_tasks = TaskSerializer(tasks, many=True)
        serializer = serializer_activity.data + serializer_pictures.data + serializer_tasks.data
        print(serializer)
        return Response(serializer)

