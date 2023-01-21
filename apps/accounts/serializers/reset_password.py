from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers


# Create your serializers here.

class SendCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()

    class Meta:
        fields = [
            'email',
        ]


class VerifyOtpSerializer(serializers.Serializer):
    otp = serializers.CharField()

    class Meta:
        fields = [
            'otp',
        ]


class ResetPasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
        validators=[validate_password],
    )

    confirm_password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
        validators=[validate_password],
    )

    class Meta:
        fields = [
            'new_password',
            'confirm_password',
        ]

    def validate(self, attrs):
        if attrs['new_password'] != attrs['confirm_password']:
            raise serializers.ValidationError({
                "password_error": "New password fields didn't match.",
            })

        return attrs
