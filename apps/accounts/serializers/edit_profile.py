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
        for attr, value in validated_data.items():
            if attr in 'address':
                try:
                    address = Address.objects.get(user=instance)
                except Address.DoesNotExist:
                    address = Address.objects.create(user=instance)

                for item, cost in value.items():
                    setattr(address, item, cost)
                address.save()
            else:
                setattr(instance, attr, value)
        instance.save()

        return instance
