from rest_framework.validators import UniqueTogetherValidator


from rest_framework import serializers
from company.models import Company, Activity, Area



class CompanySerializer(serializers.ModelSerializer):

    def create(self, validate_data):
        company = Company.objects.create(**validate_data)

        return company
    class Meta:
        model = Company
        fields = '__all__'

        validators = [
            UniqueTogetherValidator(
                queryset = Company.objects.all(),
                fields=['rfc']
            )
        ]



class AreaSerializer(serializers.ModelSerializer):

    def create(self, validate_data):
        company = Company.objects.create(**validate_data)

        return company
    class Meta:
        model = Area
        fields = '__all__'


class ActivitySerializer(serializers.ModelSerializer):

    def create(self, validate_data):
        activity = Activity.objects.create(**validate_data)

        return activity
    class Meta:
        model = Activity
        fields = '__all__'
