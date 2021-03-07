from django.shortcuts import render


from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response



from .models import Company, Area
from .serializers import CompanySerializer, AreaSerializer

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
