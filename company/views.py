from django.shortcuts import render


from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response



from .models import Company, Area, Activity
from .serializers import CompanySerializer, AreaSerializer, ActivitySerializer

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



class ActivityRecordView(APIView):
    def get(self, request, area):


        activities_area = Activity.objects.filter(area=area)
        serializer = ActivitySerializer(activities_area, many=True)

        return Response(serializer.data)
