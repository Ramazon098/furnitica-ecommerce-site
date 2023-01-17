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
            'my_name',
            'address',
            'phone_number',
        ]
