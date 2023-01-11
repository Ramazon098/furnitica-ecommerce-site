from rest_framework.serializers import Serializer


# Create your serializers here.

class EditProfileSerializer(Serializer):
    class Meta:
        fields = [
            'id',
            'my_name',
            'company',
        ]
