from rest_framework import serializers
from .models import Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['symbol', 'name', 'last_fetch']
        extra_kwargs = {
            'symbol': {'required': False},  # Ensure this is set if you're not providing 'symbol' every time
            'name': {'required': True}  # Check requirements for fields
        }
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance