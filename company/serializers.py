from rest_framework.validators import UniqueTogetherValidator


from rest_framework import serializers
from company.models import Company



class CompanySerializer(serializers.ModelSerializer):

    def create(self, validate_data):
        company = Company.objects.create(**validate_data)

        return company
    class Meta:
        model = Company
        fields = ('rfc', 'name_company', 'email', 'street')

        validators = [
            UniqueTogetherValidator(
                queryset = Company.objects.all(),
                fields=['rfc']
            )
        ]
