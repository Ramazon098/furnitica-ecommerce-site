from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from apps.accounts.models import CustomUser


# Create your serializers here.

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[
            UniqueValidator(
                CustomUser.objects.all(),
                "A user with that Email already exists.",
            ),
        ],
    )

    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    password1 = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
        validators=[validate_password],
    )

    password2 = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
        validators=[validate_password],
    )

    class Meta:
        model = CustomUser
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        ]

    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError({
                "password_error": "Password fields didn't match.",
            })
        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )

        user.set_password(validated_data['password1'])
        user.save()
        return user


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
