from django.contrib.auth import authenticate

from rest_framework import serializers

from apps.accounts.models import CustomUser


# Create your serializers here.

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
    )

    class Meta:
        model = CustomUser
        fields = [
            'id',
            'email',
            'password',
        ]

    def validate(self, attrs):
        user = authenticate(
            request=self.context['request'],
            username=attrs['email'],
            password=attrs['password'],
        )

        if user is None:
            raise serializers.ValidationError({
                "user_error": "The email or password was entered incorrectly.",
            })

        return attrs
