from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response


from .models import Company
from .serializers import CompanySerializer

class CompanyRecordView(APIView):
    #permission_classes = [IsAdminUser]
    def get(self, format=None):
        companys = Company.objects.all()
        serializer = CompanySerializer(companys, many=True)

        return Response(serializer.data)
