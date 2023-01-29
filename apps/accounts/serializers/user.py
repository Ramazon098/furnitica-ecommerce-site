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
            'image',
            'address',
            'is_staff',
            'is_superuser',
            'is_active',
        ]


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
            'image',
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
