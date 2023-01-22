from random import randint

from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers

from apps.accounts.models import CustomUser, Otp


# Create your serializers here.

class SendCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()

    class Meta:
        fields = [
            'email',
        ]

    def create(self, validated_data):
        # mavjud bo'lmaslik shartini ham ko'rish
        user = CustomUser.objects.get(email=validated_data['email'])
        random_otp = randint(100000, 999999)

        if Otp.objects.filter(otp=random_otp).exists():
            random_otp = randint(100000, 999999)

        if Otp.objects.filter(user=user).exists():
            otp_user = Otp.objects.get(user=user)
            otp_user.otp = random_otp
            otp_user.save()
        else:
            _ = Otp.objects.create(user=user, otp=random_otp)

        return validated_data


class VerifyOtpSerializer(serializers.Serializer):
    otp = serializers.CharField()

    class Meta:
        fields = [
            'otp',
        ]

    def create(self, validated_data):
        return validated_data


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

    def create(self, validated_data):
        return validated_data
