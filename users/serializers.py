from rest_framework.validators import UniqueTogetherValidator


from rest_framework import serializers
from users.models import NewUser


class UserSerializer(serializers.ModelSerializer):

    def create(self, validate_data):
        user = NewUser.objects.create_user(**validate_data)

        return user
    class Meta:
        model = NewUser
        fields = ('id_user', 'password')

        validators = [
            UniqueTogetherValidator(
                queryset = NewUser.objects.all(),
                fields=['id_user']
            )
        ]

