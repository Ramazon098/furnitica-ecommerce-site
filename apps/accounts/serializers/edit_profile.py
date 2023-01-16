from rest_framework.serializers import Serializer

from apps.accounts.models import CustomUser, Address


# Create your serializers here.

class EditProfileSerializer(Serializer):

    class Meta:
        fields = [
            'id',
            'my_name',
            'company',
        ]
