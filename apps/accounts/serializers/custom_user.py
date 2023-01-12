from rest_framework.serializers import ModelSerializer

from apps.accounts.models import CustomUser, Address


# Create your serializers here.

class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = [
            'address',
            'city',
            'country',
            'zip_code',
        ]


class CustomUserSerializer(ModelSerializer):
    address = AddressSerializer(read_only=True)

    class Meta:
        model = CustomUser
        fields = [
            'id',
            'email',
            'my_name',
            'phone_number',
            'address',
            'is_staff',
            'is_superuser',
            'is_active',
        ]
