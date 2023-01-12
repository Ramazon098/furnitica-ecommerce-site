from rest_framework import serializers

from apps.accounts.models import CustomUser, Address


# Create your serializers here.

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            'address',
            'city',
            'country',
            'zip_code',
        ]


class CustomUserSerializer(serializers.ModelSerializer):
    custom_users = AddressSerializer(read_only=True, many=True)

    # def get_address(self, obj):
    #     address = Address.objects.filter(user=obj)
    #     return AddressSerializer(instance=address).data

    class Meta:
        model = CustomUser
        fields = [
            'id',
            'email',
            'my_name',
            'phone_number',
            'custom_users',
            'is_staff',
            'is_superuser',
            'is_active',
        ]
