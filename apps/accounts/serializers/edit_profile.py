from rest_framework.serializers import ModelSerializer

from apps.accounts.serializers import AddressSerializer
from apps.accounts.models import CustomUser


# Create your serializers here.

class EditProfileSerializer(ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = CustomUser
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'phone_number',
            'address',
        ]

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
