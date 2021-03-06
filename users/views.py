from django.shortcuts import render


from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import NewUser
from .serializers import UserSerializer



class UserRecordView(APIView):
    """
    API View to create or get a list of all the registered
    users. GET request returns the registered users whereas
    a POST request allows to create a new user.
    """
    #permission_classes = [IsAdminUser]

    def get(self, request, user_id):
        users = NewUser.objects.filter(id_user=user_id)
        serializer = UserSerializer(users, many=True)

        return Response(serializer.data)


    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "error": True,
                "error_msg": serializer.error_messages,
            },
            status=status.HTTP_400_BAD_REQUEST
        )




