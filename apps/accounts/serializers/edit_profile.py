from rest_framework.serializers import ModelSerializer

from apps.accounts.serializers import AddressSerializer
from apps.accounts.models import CustomUser, Address


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
        instance.email = validated_data['email']
        instance.first_name = validated_data['first_name']
        instance.last_name = validated_data['last_name']
        instance.phone_number = validated_data['phone_number']
        instance.save()

        address = Address.objects.get(user=instance)
        address.address = validated_data['address']['address']
        address.city = validated_data['address']['city']
        address.country = validated_data['address']['country']
        address.zip_code = validated_data['address']['zip_code']
        address.save()

        return instance
